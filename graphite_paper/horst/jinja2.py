import os
from django.conf import settings
from django.contrib.staticfiles.storage import staticfiles_storage
from urllib.parse import urlencode
from django.urls import reverse

from jinja2 import Environment
from markdown import markdown

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
        share_domain="https://twitter.com/intent/tweet?",
        param="text",
        title="title",
    ),
    x=dict(
        share_domain="https://twitter.com/intent/tweet?",
        param="text",
        title="title",
    ),
    linkedin=dict(
        share_domain="https://www.linkedin.com/shareArticle?mini=true&",
        param="url",
        description="summary",
        title="title",
    ),
    whatsapp=dict(
        share_domain="https://wa.me/?",
        param="text",
    ),
    mastodon=dict(
        share_domain="https://mastodon.social/share?",
        param="text",
    ),
    bluesky=dict(
        share_domain="https://bsky.app/intent/compose?",
        param="text",
    ),
)

def get_share_domain(network_name, link, description=None, title=None):
    link = link.replace(":", "%3A")
    network = SOCIAL_NETWORKS.get(network_name)
    if not network:
        return ""
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

def get_social_share_platforms(meta):
    """Get list of social share platforms from meta.yaml, with fallback to defaults."""
    default_platforms = ['facebook', 'twitter', 'linkedin']
    
    # Check if social_share_platforms is configured in meta.yaml
    platforms = meta.get('social_share_platforms', default_platforms)
    
    # Ensure it's a list and filter out unsupported platforms
    if not isinstance(platforms, list):
        return default_platforms
    
    # Filter to only include supported platforms
    supported_platforms = [platform for platform in platforms if platform in SOCIAL_NETWORKS]
    
    # Return default if no valid platforms found
    return supported_platforms if supported_platforms else default_platforms

def media(file_reference):
    if file_reference.startswith("http"):
        return file_reference
    else:
        return os.path.join(GRAPHITE_SERVER, file_reference)

def markdown_filter(content):
    """Convert markdown to HTML."""
    return markdown(
        content,
        extensions=["markdown.extensions.tables", "markdown.extensions.nl2br"],
    )

def additional_globals():
    return dict(
        static=staticfiles_storage.url,
        settings=settings,
        DEBUG=settings.DEBUG and settings.SUPER_DEBUG,
        urlencode=urlencode,
        get_share_domain=get_share_domain,
        get_social_share_platforms=get_social_share_platforms,
        url=reverse,
        media=media,
        zip=zip,
    )

def environment(**options):

    env = Environment(**options)
    env.globals.update(additional_globals())
    env.filters['markdown'] = markdown_filter
    return env
