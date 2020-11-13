from django.conf.urls import url
from .views import report, assets, frame

urlpatterns = (
    url(r'^(?P<slug>[\w./-]+).html$', report, name="report"),
    url(r'^(?P<path>assets/.*)$', assets, name="assets"),
    url(r'^(?P<path>theme/.*)$', assets, name="theme"),
    url(r'^frame$', frame, name="frame"),
    url(r'^$', report, name="homepage"),
)
