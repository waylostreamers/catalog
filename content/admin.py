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
    RightsAgreement,
    Role,
    SoundRecording,
    Track,
    TrackContributor,
    User,
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
    RightsAgreement,
    Role,
    SoundRecording,
    Track,
    TrackContributor,
    User,
]

# Register your models here.
for model in models:
    admin.site.register(model)
