import os
import yaml

from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse

from graphite_paper.horst.helper import markdown_helper
from graphite_paper.horst.report import Report

MIME_TYPES = dict(
    png="image/png",
    jpg="image/jpeg",
    jpeg="image/jpeg",
    csv="text/csv",
    css="text/css",
    js="text/javascript",
)

def report(request, slug="index"):
    r = Report(slug, settings.PAGES_DIRECTORY)
    return render(request, "base.html", r.get_context())

def frame(request, slug="index"):
    r = Report(slug, settings.PAGES_DIRECTORY)
    return render(request, "horst/frame.html", r.get_context())

def assets(request, path):
    file_path = os.path.join(settings.PROJECT_DIRECTORY, path)
    file_extension = path.split(".")[-1]
    content_type = MIME_TYPES.get(file_extension, "")
    print("Content type: " +  content_type)
    try:
        with open(file_path, "rb") as f:
            return HttpResponse(f.read(), content_type=content_type)
    except IOError:
        return HttpResponse("%s not found" % path)

