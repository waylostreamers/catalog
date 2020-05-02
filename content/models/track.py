from django.db import models

from .soundrecording import SoundRecording
from .user import User
from .contributor import Contributor


class Track(models.Model):
    """
    A track/song. A user may upload songs and define their metadata here.
    """
    isrc = models.CharField(max_length=12)
    title = models.CharField(max_length=256)
    contributors = models.ManyToManyField(Contributor)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    purchase_cost = models.DecimalField(decimal_places=4, max_digits=6)
    stream_cost = models.DecimalField(decimal_places=4, max_digits=6)
    purchase_count = models.BigIntegerField(default=0)
    stream_count = models.BigIntegerField(default=0)
    notes = models.TextField() # Flexible text blob for extra credits/liner notes etc.
    artwork_id = models.UUIDField()
    sound_recording = models.ForeignKey(SoundRecording, on_delete=models.SET_NULL, null=True)
