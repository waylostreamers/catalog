from django.db import models

from .track import Track
from .genre import Genre
from .user import User
from .contributor import Contributor
from .location import Location
from .rightsagreement import RightsAgreement

ALBUM = 'content"."album'
ALBUM_CONTRIBUTOR = 'content"."album_contributor'
ALBUM_TRACK = 'content"."album_track'
ALBUM_GENRE = 'content"."album_genre'

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
    contributors = models.ManyToManyField(Contributor, through='AlbumContributor')
    tracks = models.ManyToManyField(Track, through='AlbumTrack')
    artwork_id = models.UUIDField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    purchase_cost = models.DecimalField(decimal_places=4, max_digits=6)
    purchase_count = models.BigIntegerField(default=0)
    label_name = models.CharField(max_length=256, null=True)
    notes = models.TextField(null=True)
    rights_agreement = models.ForeignKey(RightsAgreement, on_delete=models.SET_NULL, null=True)
    genres = models.ManyToManyField(Genre, through='AlbumGenre')
    # available_markets = models.ArrayField(models.CharField(max_length=10))
    recording_location = models.ForeignKey(
        Location, on_delete=models.SET_NULL, null=True
    )

    class Meta:
        db_table = ALBUM


class AlbumContributor(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    contributor = models.ForeignKey(Contributor, on_delete=models.CASCADE)

    class Meta:
        db_table = ALBUM_CONTRIBUTOR 

class AlbumTrack(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    track = models.ForeignKey(Track, on_delete=models.CASCADE)

    class Meta:
        db_table = ALBUM_TRACK 


class AlbumGenre(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    class Meta:
        db_table = ALBUM_GENRE 
