from django.db import models

from .user import User
from .contributor import Contributor

COMPOSITION = 'content"."composition'
COMPOSITION_CONTRIBUTOR = 'content"."composition_contributor'


class Composition(models.Model):
    """
    A track/song. A user may upload songs and define their metadata here.
    """

    iswc = models.CharField(max_length=24)
    title = models.CharField(max_length=256)
    contributors = models.ManyToManyField(Contributor, through="CompositionContributor")
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    notes = models.TextField()  # Flexible text blob for extra credits/liner notes etc.

    class Meta:
        db_table = COMPOSITION


class CompositionContributor(models.Model):
    composition = models.ForeignKey(Composition, on_delete=models.CASCADE)
    contributor = models.ForeignKey(Contributor, on_delete=models.CASCADE)

    class Meta:
        db_table = COMPOSITION_CONTRIBUTOR
