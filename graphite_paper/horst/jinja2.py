import os
from django.conf import settings
from django.contrib.staticfiles.storage import staticfiles_storage
from urllib.parse import urlencode
from django.urls import reverse

from jinja2 import Environment

try:
    GRAPHITE_SERVER = settings.GRAPHITE_SERVER
except:
    GRAPHITE_SERVER = ""

SOCIAL_NETWORKS = dict(
    facebook=dict(
        share_domain="https://www.facebook.com/sharer/sharer.php?",
        param="u",
    ),
    twitter=dict(
        share_domain="https://twitter.com/home?",
        param="status",
    ),
    linkedin=dict(
        share_domain="https://www.linkedin.com/shareArticle?mini=true&",
        param="url",
        description="summary",
        title="title",
    ),
)

def get_share_domain(network_name, link=settings.SHARE_DOMAIN, description=None, title=None):
    link = link.replace(":", "%3A")
    network = SOCIAL_NETWORKS.get(network_name)
    param = {network["param"]: link}
    param = dict()
    if description and "description" in network:
        param[network["description"]] = description
    if title and "title" in network:
        param[network["title"]] = title
    r = network["share_domain"] + network["param"] + "=" + link
    if param:
        r = r + "&" + urlencode(param)
    return r

def media(file_reference):
    if file_reference.startswith("http"):
        return file_reference
    else:
        return os.path.join(GRAPHITE_SERVER, file_reference)

def additional_globals():
    return dict(
        static=staticfiles_storage.url,
        settings=settings,
        DEBUG=settings.DEBUG and settings.SUPER_DEBUG,
        urlencode=urlencode,
        share_domain=settings.SHARE_DOMAIN,
        share_domain_full=settings.SHARE_DOMAIN_FULL,
        get_share_domain=get_share_domain,
        url=reverse,
        media=media,
        zip=zip,
    )

def environment(**options):

    env = Environment(**options)
    env.globals.update(additional_globals())
    return env
