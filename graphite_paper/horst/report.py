import os
import yaml
from django.conf import settings
from .parser import TabReader
from .helper import markdown_helper
from .entries import ReferenceDict, FigureDict

class Report:

    def __init__(
        self,
        slug="index",
        report_dir="pages",
        base_dir = settings.BASE_DIR,
        project_directory = settings.PROJECT_DIRECTORY,
    ):
        self.BASE_DIR = base_dir
        self.PROJECT_DIRECTORY = project_directory
        self.PAGES_DIRECTORY = os.path.join(settings.BASE_DIR, report_dir)
        self.TEMPLATES_DIRECTORY = os.path.join(settings.BASE_DIR, "jinja2")
        self.figures = FigureDict()
        self.references = ReferenceDict()
        self.references.import_all(self)
        self._load_meta()
        self._load_lang()
        self.tabs = self.meta.get("tabs", [])
        del(self.meta["tabs"])
        self.slug = slug
        self.partial_count = 0

    def get_partial_id(self):
        """
        Helper method for rendering consistent and unique IDs in the HTML output.
        """
        self.partial_count += 1
        return self.partial_count

    def get_context(self):
        """
        Core method: returns an dictonary with all elements to render a report
        using the appropriate Jinja2 template.
        """
        self._iterate_and_parse_tabs()
        return dict(
            slug=self.slug,
            meta=self.meta,
            tabs=self.tabs,
            lang=self.lang,
        )

    def _iterate_and_parse_tabs(self):
        for tab in self.tabs:
            tab["tabHref"] = "" if tab["slug"] == "index" else tab["slug"]
            tab["active"] = True if tab["slug"] == self.slug else False
            self.current_tab = tab
            tab["content"] = TabReader(self, tab).get_template().render()

    def _load_meta(self, slug="", meta_name="meta.yaml"):
        file_path = os.path.join(self.PROJECT_DIRECTORY, "config", meta_name)
        meta = dict(
            title="Page title",
            authors="Author1, Author2, Author3",
            year="2017",
        )
        with open(file_path, "r") as f:
            file_content = f.read()
            if meta_name[-4:] == "yaml":
                meta.update(yaml.safe_load(file_content))
        meta["abstract_md"] = markdown_helper(meta.get("abstract", ""))
        meta["slug"] = "/%s/" % slug if slug != "index" else "/"
        self.meta = meta
    
    def _load_lang(self, lang_name="lang.yaml"):
        file_path = os.path.join(self.PROJECT_DIRECTORY, "config", lang_name)
        lang = dict()
        with open(file_path, "r") as f:
            file_content = f.read()
            if lang_name[-4:] == "yaml":
                lang.update(yaml.safe_load(file_content))
        self.lang = lang
