import os, glob
from xml.etree import ElementTree
import yaml
from markdown import markdown
from jinja2 import PackageLoader, Template, Environment
from .jinja2 import additional_globals

def markdown_helper(content):
    return markdown(
        content,
        extensions=["markdown.extensions.tables"],
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
