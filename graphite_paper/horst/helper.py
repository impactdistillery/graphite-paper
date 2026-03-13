import os, glob
from xml.etree import ElementTree
import yaml
from markdown import markdown
from markdown.extensions import Extension
from markdown.treeprocessors import Treeprocessor
from jinja2 import PackageLoader, Template, Environment
from .jinja2 import additional_globals, append_to_last_p


class _ExternalLinkProcessor(Treeprocessor):
    """Open external links (http/https) in a new tab with security attributes."""

    def run(self, root):
        for el in root.iter("a"):
            href = el.get("href", "")
            if href.startswith("http://") or href.startswith("https://"):
                el.set("target", "_blank")
                el.set("rel", "noreferrer noopener")


class ExternalLinksExtension(Extension):
    """Markdown extension that adds target='_blank' and rel='noreferrer noopener'
    to all external links (http/https) in the rendered output, so user-authored
    markdown content follows the same external-link standard as the templates."""

    def extendMarkdown(self, md):
        md.treeprocessors.register(
            _ExternalLinkProcessor(md), "external_links", 5
        )


def markdown_helper(content):
    return markdown(
        content,
        extensions=[
            "markdown.extensions.tables",
            "markdown.extensions.nl2br",
            ExternalLinksExtension(),
        ],
    )

def read_report_file(report, file_name):
    file_path = os.path.join(
        report.PAGES_DIRECTORY,
        file_name,
    )
    with open(file_path, "r") as f:
        return f.read()

def jinja_template(template_html):
    #env = Environment(
    #    loader=PackageLoader("horst", "jinja2"),
    #)
    #template = env.from_string(template_html)
    template = Template(template_html)
    template.globals.update(additional_globals())
    # Add markdown filter
    template.environment.filters['markdown'] = markdown_helper
    template.environment.filters['append_to_last_p'] = append_to_last_p
    return template

def svg_remove_wh(glob_path="_build/images/*svg"):
    for file_path in glob.glob(glob_path):
        print("[INFO] Remove w/h from " + file_path)
        ElementTree.register_namespace("", "http://www.w3.org/2000/svg")
        xml = ElementTree.parse(file_path)
        svg = xml.getroot()
        for key in ["width", "height"]:
            del(svg.attrib[key])
        xml.write(file_path)
