import os
import yaml
from collections import OrderedDict
from .helper import read_report_file


class AbstractEntry:

    def __init__(self, directory, key, entry): 
        self.key = key
        self.entry = entry
        self.directory = directory
        self.directory[key] = self

    def render(self):
        return "<p><b>%s:</b> %s</p>" % (self.key, self.entry)

class AbstractDict(OrderedDict):

    def add_entry(self, key, entry):
        AbstractEntry(self, key, entry)

    def sorted_items(self):
        for key in sorted(self.keys()):
            yield key, self[key]

    def import_all(self, report, file_name=None):
        if not file_name:
            file_name = self.Meta.import_file_name
        content = read_report_file(report, file_name)
        data = yaml.safe_load(content)
        for key, value in data.items():
            self[key] = value


class ReferenceEntry(AbstractEntry):
    pass


class ReferenceDict(AbstractDict):

    class Meta:
        import_file_name = "references.yaml"

    def add_entry(self, key, entry):
        ReferenceEntry(self, key, entry)


class FigureEntry(AbstractEntry):
    pass


class FigureDict(AbstractDict): 

    def add_entry(self, key, entry):
        FigureEntry(self, key, entry)


