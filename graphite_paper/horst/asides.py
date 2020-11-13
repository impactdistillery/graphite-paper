import os
import pprint
import yaml
import pandas as pd
from .render import RenderTwo, RenderSingle
from .helper import markdown_helper, jinja_template


class AbstractAside:
    """
    Abstract class.

    Please inherit and implement:

    -   ``Meta.name`` to set the name of a aside for reference in the
        configuration.
    -   ``Meta.template`` is an optional parameter to enable the build-in
        template helper ``render_template(data)`` where ``data`` is s dict.
    -   ``pre_render()`` to generate HTML partial.
    """

    def __init__(self, report, config, requested_parser, params=None):
        self.report = report
        self.config = config
        self.params = params
        self.requested_parser = requested_parser.lower()
        self.process()

    def process(self):
        pass

    def pre_render(self):
        """
        Abstract method: render Aside to HTML.
        """

    def render(self):
        return "<aside class=\"ms-aside-%s\">%s</aside>" % (
            self.requested_parser,
            self.pre_render(),
        )

    def render_template(self, data=dict()):
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


class DefaultAside(AbstractAside):
    
    class Meta:
        name = "default"

    def pre_render(self):
        return markdown_helper(self.config)


class GlossaryAside(AbstractAside):
    
    class Meta:
        name = "glossary"

    def pre_render(self):
        x = self.config.split(":")
        if len(x) == 1:
            x = x[0]
        else:
            x = "**%s:**%s" % (x[0], ":".join(x[1:]))
        return markdown_helper(x)

class MarkdownAside(AbstractAside):
    
    class Meta:
        name = "markdown"

    def pre_render(self):
        return markdown_helper(self.config)


class KeystatementAside(MarkdownAside):
    
    class Meta:
        name = "keystatement"


class SidenoteAside(MarkdownAside):
    
    class Meta:
        name = "sidenote"

class ReferenceAside(MarkdownAside):
    
    class Meta:
        name = "reference"

    def pre_render(self):
        return markdown_helper("%s" % (
           self.report.references[self.config].get("short"),
        ))


class YamlAside(AbstractAside):

    class Meta:
        name = "yaml"

    def process(self):
        try:
            self.data = yaml.safe_load(self.config)
        except:
            self.data = dict()

    def pre_render(self):
        return "<pre>---\n%s\n---</pre>" % self.format_data()


class AsideController:

    @classmethod
    def get_all_asides(cls):
        subclasses = set()
        work = [AbstractAside]
        while work:
            parent = work.pop()
            for child in parent.__subclasses__():
                if child not in subclasses:
                    subclasses.add(child)
                    work.append(child)
        return subclasses

    @classmethod
    def get_aside_from_config(cls, config):
        if "class" in config:
            aside = cls.get_aside(config["class"])
        else:
            aside = DefaultAside
        return aside(config)
    
    @classmethod
    def get_aside(cls, name):
        for aside in cls.get_all_asides():
            if aside.Meta.name.lower() == name.lower():
                return aside
        return  DefaultAside
