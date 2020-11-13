import os
import pprint
import yaml
import pandas as pd
from .helper import jinja_template
from .render import RenderTwo, RenderSingle, Figure
from .helper import markdown_helper
from .asides import AsideController

DEFAULT_TEMPLATE = "<span class=\"ms-inline ms-inline-%s\">%s<i></i></span>"

POPOVER_TEMPLATE_FULL = "<a tabindex=\"0\" data-trigger=\"focus hover\" class=\"ms-inline ms-inline-%s\" data-toggle=\"popover\" data-placement=\"top\" title=\"%s\" data-content=\"%s\">%s<i></i></a>"

POPOVER_TEMPLATE = "<span class=\"ms-inline ms-inline-%s\">%s<i></i></span>"

class AbstractInline:
    """
    Abstract class.

    Please inherit and implement:

    -   ``Meta.name`` to set the name of a inline for reference in the
        configuration.
    -   ``Meta.template`` is an optional parameter to enable the build-in
        template helper ``render_template(data)`` where ``data`` is s dict.
    -   ``render()`` to generate HTML partial.
    """

    def __init__(self, report, data, partial):
        self.report = report
        self.data = data
        self.partial = partial
        self.process()

    def process(self):
        pass

    def render(self):
        """
        Abstract method: render Inline to HTML.
        """

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


class DefaultInline(AbstractInline):
    
    class Meta:
        name = "default"

    def render(self):
        return DEFAULT_TEMPLATE % (
            self.data[0].lower(),
            self.format_data(),
        )

class GloassaryInline(AbstractInline):
    
    class Meta:
        name = "glossary"

    def process(self):
        if len(self.data) > 2:
            self.label = self.data[2]
        else:
            self.label = self.data[1]

    def render(self):
        return POPOVER_TEMPLATE % (
            self.data[0].lower(),
            self.label,
        )

class SidenoteInline(AbstractInline):
    
    class Meta:
        name = "sidenote"

    def process(self):  
        #aside = AsideController.get_aside(self.Meta.name)
        #self.partial.asides.append(
        #    aside(self.report, self.data[1], self.Meta.name),
        #)
        if len(self.data) > 2:
            self.label = self.data[2]
        else:
            self.label = self.data[1]

    def render(self):
        return DEFAULT_TEMPLATE % (
            self.data[0].lower(),
            self.label,
        )


class ThanksInline(SidenoteInline):
    
    class Meta:
        name = "thanks"

class ReferenceInline(AbstractInline):
    
    class Meta:
        name = "reference"

    def process(self):
        #aside = AsideController.get_aside(self.Meta.name)
        #self.partial.asides.append(
        #    aside(self.report, self.data[1], self.Meta.name),
        #)
        self.reference = self.report.references.get(
            self.data[1],
            dict(),
        )
        if len(self.data) > 2:
            self.label = self.data[2]
        else:
            self.label = self.data[1]

    def render(self):
        popover_content = self.reference.get("short")
#        url = self.reference.get("url", "")
#        if url:
#            popover_content += "<a class='mdi mdi-earth' href='%s' target='_blank'></a>" % url
        return POPOVER_TEMPLATE_FULL % (
            self.data[0].lower(),
            self.report.lang.get("cited_source", "Cited source"),
            popover_content,
            self.label,
        )


class InlineController:

    @classmethod
    def get_all_inlines(cls):
        subclasses = set()
        work = [AbstractInline]
        while work:
            parent = work.pop()
            for child in parent.__subclasses__():
                if child not in subclasses:
                    subclasses.add(child)
                    work.append(child)
        return subclasses

    @classmethod
    def get_inline_from_config(cls, config):
        if "class" in config:
            inline = cls.get_inline(config["class"])
        else:
            inline = DefaultInline
        return inline(config)
    
    @classmethod
    def get_inline(cls, name):
        for inline in cls.get_all_inlines():
            if inline.Meta.name.lower() == name.lower():
                return inline
        return  DefaultInline
