import os
from .helper import jinja_template

PLUGIN_CLASS_PRE = "ms-plugin-"

class AbstractRender:

    def __init__(self, report, content, aside="", pre="", partial_id=None, plugin_class="undefined", plugin_data=None):
        self.report = report
        self.content = content
        self.aside = aside
        self.pre = pre
        self.plugin_class = PLUGIN_CLASS_PRE + plugin_class
        self.partial_id = partial_id
        self.plugin_data = plugin_data

    def render_template(self, data=dict()):
        file_path = os.path.join(
            self.report.TEMPLATES_DIRECTORY,
            self.Meta.template,
        )
        with open(file_path, "r+") as f:
            template = jinja_template(f.read())
        return template.render(data)

    def render(self):
        return self.render_template()


class Slides(AbstractRender):

    class Meta:
        template = "horst/render/slides.html"

    def render(self):
        return self.render_template(dict(
            pluginClass=self.plugin_class,
            content=self.content,
            aside=self.aside,
            partialId=self.partial_id,
        ))


class RenderTwo(AbstractRender):

    class Meta:
        template = "horst/render/two.html"
        master_tag = "div"

    def render(self):
        return self.render_template(dict(
            pluginClass=self.plugin_class,
            content=self.content,
            aside=self.aside,
            partialId=self.partial_id,
            tag="div",
        ))

class RenderThree(AbstractRender):

    class Meta:
        template = "horst/render/three.html"
        master_tag = "div"

    def render(self):
        return self.render_template(dict(
            pluginClass=self.plugin_class,
            pre=self.pre,
            content=self.content,
            aside=self.aside,
            partialId=self.partial_id,
            tag="div",
        ))

class Directory(RenderTwo):

    class Meta:
        template = "horst/render/directory.html"


class Figure(RenderTwo):

    class Meta:
        template = "horst/render/two.html"
        master_tag = "figure"

    def render(self, full=False):
        return self.render_template(dict(
            pluginClass=self.plugin_class,
            content=self.content,
            aside=self.aside,
            partialId=self.partial_id,
            tag="figure",
            full=full,
        ))


class FullFigure(Figure):
    
    def render(self, full=True):
        return super().render(full=full)

class Section(RenderTwo):

    class Meta:
        template = "horst/render/section.html"
        master_tag = "section"

    def render(self):
        return self.render_template(dict(
            pluginClass=self.plugin_class,
            content=self.content,
            aside=self.aside,
            partialId=self.partial_id,
        ))

class RenderText(RenderTwo):

    class Meta:
        template = "horst/render/text.html"


class RenderSingle(AbstractRender):

    class Meta:
        template = "horst/render/single.html"

    def render(self):
        return self.render_template(dict(
            pluginClass=self.plugin_class,
            content=self.content,
            partialId=self.partial_id,
        ))

class RenderFullWidth(RenderSingle):

    class Meta:
        template = "horst/render/full.html"

class RenderChapterHeader(RenderSingle):

    class Meta:
        template = "horst/render/chapter-header.html"

    def render(self):
        try:
            image = self.plugin_data["image"]
        except:
            image = None
        return self.render_template(dict(
            pluginClass=self.plugin_class,
            content=self.content,
            partialId=self.partial_id,
            image=image,
        ))
