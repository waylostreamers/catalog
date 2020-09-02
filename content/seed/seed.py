import uuid
import json
from typing import List

from faker import Faker
from django.core import serializers
from django.db import transaction

from .providers import TitleProvider, RoleProvider, ISRCProvider
from .artists import create_artist

from ..models import (
    Album,
    Artist,
    Composition,
    Contributor,
    Genre,
    Location,
    Roles,
    SoundRecording,
    Track,
    User,
)

faker = Faker()
faker.add_provider(TitleProvider)
faker.add_provider(RoleProvider)
faker.add_provider(ISRCProvider)


@transaction.atomic
def seed(users):
    print("Seeding database...")
    users = [create_user() for n in range(users)]
    user_map = {user.id: {"user": user} for user in users}
    for user in users:
        num_artists = faker.random.randint(1, 10)
        artists = [create_artist(user, True) for n in range(num_artists)]
        [artist.save() for artist in artists]
        num_albums = faker.random.randint(1, 5)
        create_user_albums(num_albums, user, artists)
    print(f"Generated {len(users)} users with randomized track and album data.")


def create_user_albums(n, user, artists):
    for i in range(n):
        album_artists = artists
        track_artists = artists
        num_tracks = faker.random.randint(1, 10)
        tracks = [create_track(user, artists) for n in range(num_tracks)]
        album = create_album(user, tracks, album_artists)


def create_user():
    user = User(
        email=faker.email(),
        first_name=faker.first_name(),
        last_name=faker.last_name(),
        location=create_location(),
    )
    user.save()
    return user


def create_contributor(artist, role=None):
    contributor = Contributor(artist=artist, role=role or faker.role())
    contributor.save()
    return contributor


def create_track(user, artists=List):
    track = Track(
        isrc=faker.isrc(),
        title=faker.title(),
        owner=user,
        purchase_cost=1,
        stream_cost=0.01,
        composition=create_composition(user),
    )
    track.save()
    contributors = [create_contributor(artist, faker.role()) for artist in artists]
    [track.contributors.add(contributor) for contributor in contributors]
    return track


def create_album(user, tracks, artists):
    album = Album(
        upc=faker.upc_a(),
        title=faker.title(),
        artwork_id=faker.uuid4(),
        owner=user,
        purchase_cost=10,
    )
    album.save()
    contributors = [create_contributor(artist, faker.role()) for artist in artists]
    [album.contributors.add(contributor) for contributor in contributors]
    [album.tracks.add(track) for track in tracks]
    return album


def create_location():
    location = Location(
        address_one=faker.street_address(), city=faker.city(), country=faker.country()
    )
    location.save()
    return location


def create_composition(user):
    composition = Composition(title=faker.title(), owner=user)
    composition.save()
    return composition
