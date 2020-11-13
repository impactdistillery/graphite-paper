import os
import pprint
import json
import yaml
import markdown
import pandas as pd
from .render import RenderThree, RenderTwo, RenderSingle, Figure, FullFigure, Section, Directory, RenderFullWidth, Slides, RenderChapterHeader
from .helper import markdown_helper, jinja_template

class AbstractPlugin:
    """
    Abstract class.

    Please inherit and implement:

    -   ``Meta.name`` to set the name of a plugin for reference in the
        configuration.
    -   ``Meta.template`` is an optional parameter to enable the build-in
        template helper ``render_template(data)`` where ``data`` is s dict.
    -   ``render()`` to generate HTML partial.
    """

    def __init__(self, report, config, params=None, partial_id=None):
        self.report = report
        self.config = config
        self.params = params
        self.partial_id = partial_id
        self.process()

    def process(self):
        pass

    def render(self):
        """
        Abstract method: render Plugin to HTML.
        """

    def render_template(self, data=dict(), aside=False, file_name=None):
        if file_name:
            pass
        elif aside:
            file_name = self.Meta.template_aside
        else:
            file_name = self.Meta.template
        file_path = os.path.join(
            self.report.TEMPLATES_DIRECTORY,
            file_name,
        )
        with open(file_path, "r+") as f:
            template = jinja_template(f.read())
        return template.render(data)

    def format_data(self):
        return pprint.pformat(self.data)


class DefaultPlugin(AbstractPlugin):
    
    class Meta:
        name = "default"

    def render(self):
        content = "<pre>---\n%s\n---</pre>" % self.config
        aside = "<p>Standard aside</p>"
        return RenderTwo(self.report, content, partial_id=self.partial_id, plugin_class=self.Meta.name).render()


class YamlPlugin(AbstractPlugin):

    class Meta:
        name = "yaml"

    def process(self):
        try:
            self.data = yaml.safe_load(self.config)
        except:
            self.data = dict()
        if "description" in self.data:
            self.data["html_description"] = markdown.markdown(
                self.data["description"]
            )

    def render(self):
        content = "<pre>---\n%s\n---</pre>" % self.format_data()
        aside = "<p>%s</p>" % self.Meta.name
        return RenderTwo(
            self.report,
            content,
            aside,
            partial_id=self.partial_id,
            plugin_class=self.Meta.name,
        ).render()


class JsonPlugin(YamlPlugin):

    class Meta:
        name = "json"

    def process(self):
        try:
            self.data = json.loads(self.config)
        except:
            print("[ERROR] " + self.config)
            self.data = dict()


class SlidePlugin(YamlPlugin):
    
    class Meta:
        name = "slides"
        template = "horst/plugins/slides.html"

    def process(self):
        slides = self.config.split("\n---\n")
        self.slides = list()
        i = 0
        for slide in slides:
            config = yaml.safe_load(slide)
            for key, value in config.items():
                i = i + 1
                slide_content = PluginController.get_plugin(key)(
                    self.report, yaml.dump(value), partial_id="%s_%s" % (self.partial_id, i)
                ).render()
                self.slides.append((i, slide_content,))

    def render(self):
        content = self.render_template(dict(
            slides=self.slides,
            partial_id=self.partial_id,
        ))
        aside = ""
        return Slides(
            self.report,
            content,
            aside,
            partial_id=self.partial_id,
            plugin_class=self.Meta.name
        ).render()

class YamlMdPlugin(AbstractPlugin):

    class Meta:
        name= "yamlmd"

    def process(self):
        try:
            config = self.config.split("\n---\n")
            self.data = yaml.safe_load(config[0])
            self.content = markdown_helper("\n---\n".join(config[1:]))
        except:
            self.data = dict()
            self.content = ""

    def render(self):
        content = self.content
        aside = "<pre>---\n%s\n---</pre>" % self.data
        return RenderTwo(
            self.report,
            content,
            aside,
            partial_id=self.partial_id,
            plugin_class=self.Meta.name
        ).render()


class InfoboxPlugin(YamlMdPlugin):
    
    class Meta:
        name = "infobox"
        template = "horst/plugins/infobox.html"
        template_aside = "horst/plugins/infobox_aside.html"

    def process(self):
        super().process()
        link = self.data.get("link", list())
        if not link.__class__ == list:
            link = [link]
        self.data["link"] = link

    def render(self):
        content = self.render_template(dict(content=self.content))
        aside = self.render_template(self.data, aside=True)
        return Section(
            self.report,
            content,
            aside,
            partial_id=self.partial_id,
            plugin_class=self.Meta.name
        ).render()

class ArticleTopPlugin(YamlPlugin):
    
    class Meta:
        name = "article_top"
        template = "horst/plugins/article_top.html"
        template_aside = "horst/plugins/article_top_aside.html"

    def process(self):
        super().process()
        self.data["meta"] = self.report.meta
        self.data["lang"] = self.report.lang

    def render(self):
        data = self.data.copy()
        data["data"] = self.data
        data["formated_data"] = self.format_data()
        data["id"] = "quote_%s_" % self.partial_id
        content = self.render_template(data)
        aside = self.render_template(data, aside=True)
        return RenderTwo(
            self.report,
            content,
            aside,
            partial_id=self.partial_id,
            plugin_class=self.Meta.name,
        ).render()


class QuotePlugin(YamlPlugin):

    class Meta:
        name = "quote"
        template = "horst/plugins/quote.html"
        template_aside = "horst/plugins/quote_aside.html"

    def render(self):
        data = self.data.copy()
        data["data"] = self.data
        data["lang"] = self.report.lang
        data["formated_data"] = self.format_data()
        data["id"] = "quote_%s_" % self.partial_id
        content = self.render_template(data)
        aside = self.render_template(data, aside=True)
        return RenderTwo(
            self.report,
            content,
            aside,
            partial_id=self.partial_id,
            plugin_class=self.Meta.name,
        ).render()

class AuthorPlugin(YamlPlugin):

    class Meta:
        name = "author"
        template = "horst/plugins/author.html"
        template_aside = "horst/plugins/author_aside.html"

    def render(self):
        data = self.data.copy()
        data["data"] = self.data
        data["lang"] = self.report.lang
        data["formated_data"] = self.format_data()
        content = self.render_template(data)
        aside = self.render_template(data, aside=True)
        pre = self.render_template(data, file_name="horst/plugins/author_pre.html")
        return RenderThree(
            self.report,
            content,
            aside,
            pre=pre,
            partial_id=self.partial_id,
            plugin_class=self.Meta.name,
        ).render()


class ChapterHeaderPlugin(YamlPlugin):

    class Meta:
        name = "chapter_header"
        template = "horst/plugins/chapter_header.html"

    def render(self):
        data = self.data.copy()
        data["data"] = self.data
        data["lang"] = self.report.lang
        data["formated_data"] = self.format_data()
        data["id"] = "%s" % self.partial_id
        content = self.render_template(data)
        return RenderChapterHeader(
            self.report,
            content,
            partial_id=self.partial_id,
            plugin_class=self.Meta.name,
            plugin_data=self.data
        ).render()


class VideoPlugin(YamlPlugin):

    class Meta:
        name = "video"
        template = "horst/plugins/video.html"
        template_aside = "horst/plugins/video_aside.html"

    def render(self):
        data = self.data.copy()
        data["data"] = self.data
        if "youtube.com" in self.data.get("url"):
            data["youtube_id"] = self.data.get("url").replace("https://www.youtube.com/embed/", "") #TODO
        data["formated_data"] = self.format_data()
        data["config"] = self.config
        content = self.render_template(data)
        aside = self.render_template(data, aside=True)
        return RenderTwo(
            self.report,
            content,
            aside,
            partial_id=self.partial_id,
            plugin_class=self.Meta.name,
        ).render()

class FigurePlugin(YamlPlugin):

    class Meta:
        name = "figure"
        template = "horst/plugins/figure.html"
        template_aside = "horst/plugins/figure_aside.html"
        renderer = Figure

    def process(self):
        super().process()
        self.report.figures.add_entry(
            self.partial_id,
            self,
        )

    def render(self):
        data = self.data.copy()
        data["formated_data"] = self.format_data()
        data["config"] = self.config
        data["partial_id"] = self.partial_id
        data["lang"] = self.report.lang
        if data["file"].endswith("svg"):
            data["share_file"] = data["file"][:-3] + "png"
        else:
            data["share_file"] = data["file"]
        content = self.render_template(data)
        aside = self.render_template(data, aside=True)
        return self.Meta.renderer(
            self.report,
            content,
            aside,
            partial_id=self.partial_id,
            plugin_class=self.Meta.name,
        ).render()

    def __str__(self):
        return self.format_data()


class FullFigurePlugin(FigurePlugin):
    
    class Meta:
        name = "full_figure"
        template = "horst/plugins/figure.html"
        template_aside = "horst/plugins/figure_aside.html"
        renderer = FullFigure


class ListOfFiguresPlugin(YamlPlugin):

    class Meta:
        name = "listoffigures"
        template = "horst/plugins/listoffigures.html"
        template_aside = "horst/plugins/listof_aside.html"

    def get_entries(self):
        return self.report.figures

    def render(self):
        data = self.data.copy()
        data["entries"] = self.get_entries()
        content = self.render_template(data)
        aside = self.render_template(data, aside=True)
        return Directory(
            self.report,
            content,
            aside,
            partial_id=self.partial_id,
            plugin_class=self.Meta.name,
        ).render()


class ListOfReferencesPlugin(ListOfFiguresPlugin):

    class Meta:
        name = "listofreferences"
        template = "horst/plugins/listofreferences.html"
        template_aside = "horst/plugins/listof_aside.html"

    def get_entries(self):
        references = self.report.references
        for key, value in references.items():
            references[key]["html"] = markdown_helper(value.get("long"))
        return references


class VariablePlugin(JsonPlugin):

    class Meta:
        name = "variable"
        template = "horst/plugins/variable.html"
        template_aside = "horst/plugins/variable_aside.html"

    def render(self):
        data = self.data.copy()
        data["formated_data"] = self.format_data()
        data["config"] = self.config
        content = self.render_template(data)
        aside = self.render_template(data, aside=True)      
        return RenderTwo(
            self.report,
            content,
            aside,
            partial_id=self.partial_id,
            plugin_class=self.Meta.name,
        ).render()

class CsvPlugin(YamlPlugin):

    class Meta:
        name="csv"
        template = "horst/plugins/table.html"
        template_aside = "horst/plugins/table_aside.html"

    def render(self):
        file_path = os.path.join(
            self.report.PROJECT_DIRECTORY,
            self.data["file"],
        )
        data_frame = pd.read_csv(file_path)
        data = self.data.copy()
        data["lang"] = self.report.lang
        data["data_frame"] = data_frame
        data["html_table"] = data_frame.to_html(
            classes="table table-hover",
            border=0,
            index=False,
        ).replace(
            "<thead>",
            "<thead class=\"thead-inverse\">",
        )
        content = self.render_template(data)
        aside = self.render_template(data, aside=True)
        return RenderTwo(
            self.report,
            content,
            aside,
            partial_id=self.partial_id,
            plugin_class="table",
        ).render()

class HtmlPlugin(AbstractPlugin):

    class Meta:
        name = "html"

    def render(self):
        return self.config

class PluginController:

    @classmethod
    def get_all_plugins(cls):
        subclasses = set()
        work = [AbstractPlugin]
        while work:
            parent = work.pop()
            for child in parent.__subclasses__():
                if child not in subclasses:
                    subclasses.add(child)
                    work.append(child)
        return subclasses

    @classmethod
    def get_plugin_from_config(cls, config):
        if "class" in config:
            plugin = cls.get_plugin(config["class"])
        else:
            plugin = DefaultPlugin
        return plugin(config)
    
    @classmethod
    def get_plugin(cls, name):
        for plugin in cls.get_all_plugins():
            if plugin.Meta.name.lower() == name.lower():
                return plugin
        return  DefaultPlugin
