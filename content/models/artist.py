from django.db import models
from django.contrib.postgres.fields import ArrayField

from .user import User
from .location import Location

class Artist(models.Model):
    """
    A person or group of people involved in making art. "Owned" (i.e. administered by) a User.
    """
    artwork_id = models.UUIDField(null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True)
    birth_location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        related_name='birth_location',
        null=True
    )
    current_location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        related_name='current_location',
        null=True
    )
    gender = models.CharField(max_length=256, null=True)
    nationality = models.CharField(max_length=256, null=True)
    bio = models.TextField(null=True)
    external_urls = ArrayField(
        models.CharField(max_length=256)
    )


class Alias(models.Model):
    """
    Sometimes artists can be known by more than one name,
    so we allow multiple aliases to be tied back to an artist.
    Every artist must have a single "default" alias, however.
    """
    name = models.CharField(max_length=256)
    default = models.BooleanField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)


