from django.db import models
from django.conf import settings
from django.contrib.postgres.fields import ArrayField

from .location import Location


class Artist(models.Model):
    """
    A person or group of people involved in making art. "Owned" (i.e. administered by) a User.
    """

    artwork_id = models.UUIDField(null=True)
    isni = models.CharField(max_length=16, null=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True)
    birth_location = models.ForeignKey(
        Location, on_delete=models.SET_NULL, related_name="birth_location", null=True
    )
    current_location = models.ForeignKey(
        Location, on_delete=models.SET_NULL, related_name="current_location", null=True
    )
    gender = models.CharField(max_length=256, null=True)
    nationality = models.CharField(max_length=256, null=True)
    bio = models.TextField(null=True)
    external_urls = ArrayField(models.CharField(max_length=256, null=True), null=True)

    @property
    def name(self):
        return self.alias_set.get(default=True).name

    def other_aliases(self):
        return self.alias_set.filter(default=False)

    def has_other_aliases(self):
        return self.alias_set.filter(default=False).exists()

    def album_contributions(self):
        return self.contributor_set.filter(albumcontributor__isnull=False).all()

    def track_contributions(self):
        return self.contributor_set.filter(trackcontributor__isnull=False).all()

    class Meta:
        db_table = 'content"."artist'


class Alias(models.Model):
    """
    Sometimes artists can be known by more than one name,
    so we allow multiple aliases to be tied back to an artist.
    Every artist must have a single "default" alias, however.
    """

    name = models.CharField(max_length=256)
    default = models.BooleanField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'content"."alias'
