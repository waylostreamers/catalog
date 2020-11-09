from django import template
from django.core.files.storage import default_storage

register = template.Library()


@register.filter()
def presigned_url(value):
    return default_storage.url("club_sandwich.mp3")
