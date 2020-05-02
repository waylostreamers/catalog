from django.db import models

from .track import Track
from .genre import Genre
from .user import User
from .contributor import Contributor
from .location import Location


class Album(models.Model):
    """
    An album is a collection of one or more tracks.
    It also associates various other metadata as shown here.
    """

    upc = models.IntegerField()
    title = models.CharField(max_length=256)
    release_date = models.DateField()
    upload_date = models.DateField()
    remaster_date = models.DateField(null=True)
    start_datetime = models.DateField()
    artists = models.ManyToManyField(Contributor)
    tracks = models.ManyToManyField(Track)
    artwork_id = models.UUIDField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    purchase_cost = models.DecimalField(decimal_places=4, max_digits=6)
    purchase_count = models.BigIntegerField(default=0)
    label_name = models.CharField(max_length=256, null=True)
    notes = models.TextField(null=True)
    # rights_agreement = models.ManyToManyField(Rights_Agreement)
    genres = models.ManyToManyField(Genre)
    # available_markets = models.ArrayField(models.CharField(max_length=10))
    recording_location = models.ForeignKey(
        Location, on_delete=models.SET_NULL, null=True
    )
