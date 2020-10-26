from django.contrib import admin

from .models import (
    Album,
    AlbumContributor,
    AlbumTrack,
    AlbumGenre,
    Artist,
    Alias,
    Contributor,
    Genre,
    Location,
    Role,
    SoundRecording,
    Track,
    TrackContributor,
    Composition,
    CompositionContributor,
)

models = [
    Album,
    AlbumContributor,
    AlbumTrack,
    AlbumGenre,
    Artist,
    Alias,
    Contributor,
    Genre,
    Location,
    Role,
    SoundRecording,
    Track,
    TrackContributor,
    Composition,
    CompositionContributor,
]

# Register your models here.
for model in models:
    admin.site.register(model)
