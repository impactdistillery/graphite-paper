import re, os, sys
import pprint

from .render import RenderSingle, RenderTwo, RenderChapterHeader, RenderText
from .plugins import PluginController
from .inlines import InlineController
from .asides import AsideController
from .helper import markdown_helper, jinja_template


MD_EXTENSION = "md"
RE_HEADING = re.compile(r'<h([0-9]+)(.*)</h([0-9]+)>')
RE_INLINE = re.compile(r'\[:([^\]]+):\]')
RE_PLUGIN_START = re.compile(r':-[-]+([^-]+)-[-]+:')
RE_PLUGIN_END = re.compile(r':--[-]+:')


class Import:

    def __init__(self, report, command, core_parser):
        self.report = report
        self.command = command
        params = [ x.strip() for x in command.split("|") ]
        if len(params) == 1:
            self.parser = core_parser
            self.file_name = params[0]
            self.attributes = None
        else:
            self.parser = PluginController.get_plugin(params[0])
            self.file_name = params[1]
            self.attributes = params[2:]
        self.read_file()

    def read_file(self):
        file_path = os.path.join(
            self.report.PAGES_DIRECTORY,
            self.file_name,
        )
        with open(file_path, "r+") as f:
            self.file_content = f.read()

    def render(self, partial_id):
        return self.parser(self.report, self.file_content).render()

    def __str__(self):
        return "+--- IMPORT ---\n+\n+   %s\n+\n+--------------" % self.command


class Partial:
    def __init__(self, report, parser="md", content="", renderer=RenderTwo):
        self.report = report
        self.parser_name = parser.lower().split("|")[0]
        self.parser = parser
        self.content = content
        self.renderer = renderer
        self.asides = list()
        self.named_heading_ids = dict()  # Maps heading position to named ID
        self.heading_counter = 0  # Track heading position for named ID mapping


    def _extract_named_heading_ids(self, content):
        """
        Extract named heading IDs from markdown content.
        
        Converts headings like "## My Heading {#my-id}" to "## My Heading"
        and stores the mapping of heading position to named ID.
        
        Returns the cleaned content with named IDs removed.
        """
        lines = content.split('\n')
        cleaned_lines = []
        heading_position = 0
        
        # Regex to match named IDs at end of heading line
        named_id_regex = re.compile(r'^(#+\s+.*?)\s*\{#([^}]+)\}\s*$')
        
        for line in lines:
            if line.strip().startswith('#'):
                match = named_id_regex.match(line)
                if match:
                    # Found a named ID
                    heading_text = match.group(1).strip()
                    named_id = match.group(2)
                    self.named_heading_ids[heading_position] = named_id
                    cleaned_lines.append(heading_text)
                else:
                    # Regular heading without named ID
                    cleaned_lines.append(line)
                heading_position += 1
            else:
                cleaned_lines.append(line)
        
        return '\n'.join(cleaned_lines)

    def render(self, partial_id):
        if self.parser_name == "md":
            # Extract named heading IDs before markdown processing
            cleaned_content = self._extract_named_heading_ids(self.content)
            html_content = markdown_helper(cleaned_content).strip()
            self.partial_id = partial_id
            renderer, html_content = self.modify_markdown_based_html(html_content)
            result = renderer(
                self.report,
                html_content,
                "\n".join([ x.render() for x in self.asides ]),
                partial_id=partial_id,
                plugin_class="md",
            ).render()
        else:
            plugin = PluginController.get_plugin(self.parser_name)
            result = plugin(
                self.report,
                self.content,
                self.parser,
                partial_id=partial_id,
            ).render()
        return result

    def modify_markdown_based_html(self, html):
        html = html.replace("<img", "<img class=\"img-fluid\"")
        html = RE_HEADING.sub(self._heading_replace, html)
        html = RE_INLINE.sub(self._inline_replace, html)
        if html.strip().startswith("<h2") and self.report.current_tab.get("md_container", "") == "article":
            renderer = RenderChapterHeader
        else:
            renderer = RenderText
        return renderer, html

    def _inline_replace(self, match):
        data = [ x.strip() for x in match.group(1).split("|")]
        inline = InlineController.get_inline(data[0])
        return inline(self.report, data, self).render()
        
    def _heading_replace(self, match):
        level = int(match.group(1)) + 1
        
        # Check if we have a named ID for this heading position
        if self.heading_counter in self.named_heading_ids:
            heading_id = self.named_heading_ids[self.heading_counter]
        else:
            # Fall back to numeric ID for backward compatibility
            partial_id = getattr(self, 'partial_id', 'unknown')
            heading_id = "heading-%s" % partial_id
        
        self.heading_counter += 1
        return "<h%s id='%s' %s</h%s>" % (level, heading_id, match.group(2), level)
    

class Aside:
    def __init__(self, report, parser="", content=""):
        self.report = report
        self.parser = parser.lower().split("|")[0].strip()
        self.content = content

    def render(self):
        html_content = markdown_helper(self.content).strip()
        renderer, html_content = self.modify_markdown_based_html(html_content)
        aside = AsideController.get_aside(self.parser)
        return aside(self.report, html_content, self.parser).render()
#        return aside(self.report, self.content, self.parser).render()

    def modify_markdown_based_html(self, html):
        html = RE_INLINE.sub(self._inline_replace, html)
        renderer = RenderText
        return renderer, html

    def _inline_replace(self, match):
        data = [ x.strip() for x in match.group(1).split("|")]
        inline = InlineController.get_inline(data[0])
        return inline(self.report, data, self).render()


class CoreParser:
    """
    This is the core class for parsing our Markdown files, including the
    special syntax::

        :--- PLUGIN ---:
        yaml: code
        :--------------:
    """

    #TODO There might be an issue with blank lines in lists...

    #TODO Parsing aside plugins
    #     --> including directly linked ones...

    def __init__(self, report, input_text):
        self.report = report
        self.input_text = input_text
        self.content = self._generate_content_list()

    def _generate_content_list(self):
        plugin = None         # Indicator for parsing a plugin
        code = False          # Indicator for parsing code snippets
        plugin_first = False  # Indicator for the first line within a plugin
        after_blank = False   # Indicator for the first line of a partial
        partial = list()
        aside = False
        config = list()
        results = list()

        for line in self.input_text.split("\n"):

            # (1) Deal with plugins (incl. file imports and side notes)
            if RE_PLUGIN_START.match(line):
                if aside:
                    results[-1].asides.append(
                        Aside(self.report, plugin, "\n".join(config))
                    )
                plugin = RE_PLUGIN_START.sub("\\1", line).strip()
                config = list()
                plugin_first = True
                if not after_blank and not aside:
                    aside = True
                    if len(partial) > 0:
                        results.append(Partial(self.report, "md", "\n".join(partial)))
                    partial = list()
            elif plugin:
                if RE_PLUGIN_END.match(line):
                    if aside:
                        results[-1].asides.append(
                            Aside(self.report, plugin, "\n".join(config))
                        )
                        aside = False
                    else:
                        results.append(Partial(self.report, plugin, "\n".join(config),))
                    config = list()
                    aside = False
                    plugin = None
                elif plugin_first and line == "":
                    results.append(Import(self.report, plugin, self.__class__))
                    config = list()
                    plugin = None
                else:
                    config.append(line)
                    plugin_first = False

            # (2) Deal with code snippets (currently treated as markdown)
            elif line.startswith("```") and not code:
                partial = list()
                code = True
            elif code:
                if line.startswith("```"):
                    code = False
                    results.append(Partial(self.report, "code", "\n".join(partial)))
                    partial = list()
                else:
                    partial.append(line)

            # (3) Deal with normal markdown
            elif line == "":
                if len(partial) > 0:
                    results.append(Partial(self.report, "md", "\n".join(partial)))
                partial = list()
                aside = False
            else:
                partial.append(line)

            # Set after_blank
            after_blank = True if line == "" else False

        results.append(Partial(self.report, "md", "\n".join(partial), ))
        return results

    def render(self):
        rendered_content = list()
        for partial in self.content:
            rendered_content.append(partial.render(
                self.report.get_partial_id()
            ))
        return "\n".join(rendered_content)

    def __str__(self):
        return "\n\n".join([
            str(x) for x in self.content
        ])


class TabReader:

    def __init__(self, report, tab):
        self.report = report
        slug = tab.get("slug", "")
        print("[INFO] Processing slug: " + slug)
        file_path = os.path.join(
            self.report.PAGES_DIRECTORY,
            "%s.%s" % (slug, MD_EXTENSION),
        )
        self.content = self.read_file(file_path)

    def read_file(self, filepath):
        with open(filepath, "r") as f:
            return f.read()

    def parse(self):
        return CoreParser(self.report, self.content).render()

    def get_template(self):
        return jinja_template(self.parse())
