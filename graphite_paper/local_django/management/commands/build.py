import os
import shutil

from django.conf import settings
from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.core.urlresolvers import reverse
from django.test.client import Client

from horst.helper import svg_remove_wh

class Command(BaseCommand):
    help = "Build static site output"
    leave_local_alone = True

    def handle(self, *args, **options):
        """
        Request pages and build output.
        """
        if os.path.exists(settings.OUTPUT_DIRECTORY):
            shutil.rmtree(settings.OUTPUT_DIRECTORY)
        os.mkdir(settings.OUTPUT_DIRECTORY)
        os.makedirs(settings.STATIC_ROOT, exist_ok=True)
        self._collectstatic()
        client = Client()
        output_dir = settings.OUTPUT_DIRECTORY
        response = client.get("/")
        with open(os.path.join(output_dir, "index.html"), "wb") as f:
            f.write(response.content)
        response = client.get("/frame")
        with open(os.path.join(output_dir, "frame.html"), "wb") as f:
            f.write(response.content)
        self._copy_directory("assets")
        self._copy_directory("theme")
        svg_remove_wh()

    def _collectstatic(self):
        print("[INFO] Collect static")
        call_command("collectstatic", interactive=False, clear=True, verbosity=0)

    def _copy_directory(self, path):
        print("[INFO] Copy %s/" % path)
        input_path = os.path.join(
            settings.PROJECT_DIRECTORY,
            path,
        )
        output_path = os.path.join(
            settings.OUTPUT_DIRECTORY,
            path,
        )
        os.system("rm -rf %s" % output_path)
        os.system("cp -r %s %s" % (input_path, output_path))

