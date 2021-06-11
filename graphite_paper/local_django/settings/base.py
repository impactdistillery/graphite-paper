import sys, os

SHARE_DOMAIN="http://idist.io/g/sum/"
SHARE_DOMAIN_FULL="https://www.impactdistillery.com/graphite/hiig-sum/"

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

if "build" in sys.argv:
    STATIC_URL = "static/"
else:
    STATIC_URL = "/static/"

SECRET_KEY="whatever"

ROOT_URLCONF="graphite_paper.local_django.urls"

MIDDLEWARE_CLASSES=()

INSTALLED_APPS=(
    "django.contrib.staticfiles",
    "graphite_paper.local_django",
    "graphite_paper.horst",
)

TEMPLATES=(
    dict(
        BACKEND="django.template.backends.jinja2.Jinja2",
        DIRS=[
            os.path.join(BASE_DIR, "jinja2"),
        ],
        APP_DIRS=True,
        OPTIONS=dict(
            environment="graphite_paper.horst.jinja2.environment",
        ),
    ),
)

PAGES_DIRECTORY=os.path.join(BASE_DIR, "pages")

OUTPUT_DIRECTORY=os.path.join(BASE_DIR, "_build")

OUTPUT_FORMAT="HTML", #TODO enable and implement LaTeX outpu

#TEMPLATES_DIRECTORY=os.path.join(BASE_DIR, "horst/templates")

STATIC_ROOT=os.path.join(BASE_DIR, "_build", "static")

BUILD=True if "build" in sys.argv else False

