from django.urls import re_path
from .views import report, assets, frame

urlpatterns = (
    re_path(r'^(?P<slug>[\w./-]+).html$', report, name="report"),
    re_path(r'^(?P<path>assets/.*)$', assets, name="assets"),
    re_path(r'^(?P<path>theme/.*)$', assets, name="theme"),
    re_path(r'^frame$', frame, name="frame"),
    re_path(r'^$', report, name="homepage"),
)
