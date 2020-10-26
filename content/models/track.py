from django.db import models
from django.conf import settings

from .soundrecording import SoundRecording
from .composition import Composition
from .contributor import Contributor

TRACK = 'content"."track'
TRACK_CONTRIBUTOR = 'content"."track_contributor'


class Track(models.Model):
    """
    A track/song. A user may upload songs and define their metadata here.
    """

    isrc = models.CharField(max_length=12)
    title = models.CharField(max_length=256)

    contributors = models.ManyToManyField(Contributor, through="TrackContributor")
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    purchase_cost = models.DecimalField(decimal_places=4, max_digits=6, null=True)
    stream_cost = models.DecimalField(decimal_places=4, max_digits=6, null=True)
    purchase_count = models.BigIntegerField(default=0)
    stream_count = models.BigIntegerField(default=0)
    notes = models.TextField(
        null=True
    )  # Flexible text blob for extra credits/liner notes etc.
    composition = models.ForeignKey(Composition, on_delete=models.SET_NULL, null=True)
    sound_recording = models.ForeignKey(
        SoundRecording, on_delete=models.SET_NULL, null=True
    )

    class Meta:
        db_table = TRACK


class TrackContributor(models.Model):
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    contributor = models.ForeignKey(Contributor, on_delete=models.CASCADE)

    class Meta:
        db_table = TRACK_CONTRIBUTOR
