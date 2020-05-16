import uuid
import json
from typing import List

from faker import Faker
from django.core import serializers

from .providers import TitleProvider, RoleProvider, ISRCProvider
# are all these models needed to seed ?
from ..models import Album, Artist, Composition, Contributor, Genre, Location, Role, SoundRecording, Track, User

faker = Faker()
faker.add_provider(TitleProvider)
faker.add_provider(RoleProvider)
faker.add_provider(ISRCProvider)

CONTRIBUTOR_ROLES = ["primary", "featured"]


def seed(users):
    users = [create_user() for n in range(users)]
    [user.save() for user in users]
    user_map = {user.id: {"user": user} for user in users}
    create_roles()
    for user in users:
        num_artists = faker.random.randint(1, 10)
        artists = [create_artist(user) for n in range(num_artists)]
        [artist.save() for artist in artists]
        num_albums = faker.random.randint(1, 5)
        create_user_albums(num_albums, user, artists)
        print("user created")


def create_user_albums(n, user, artists):
    for i in range(n):
        album_artists = artists
        track_artists = artists
        num_tracks = faker.random.randint(1, 10)
        tracks = [create_track(user, artists) for n in range(num_tracks)]
        album = create_album(user, tracks, album_artists)


def create_user():
    return User(
        email=faker.email(), first_name=faker.first_name(), last_name=faker.last_name()
        # added location
        location = create_location()
    )


def create_artist(user):
   # return Artist(name=faker.name(), owner=user)
    return Artist( owner=user, current_location = create_location(), birth_location = create_location()
    )


def create_roles():
    roles = [Role(description=desc) for desc in CONTRIBUTOR_ROLES]
    [role.save() for role in roles]


def create_contributor(artist, role=None):
    return Contributor(artist=artist, role=role or faker.role())


def create_track(user, artists=List):
    track = Track(
        isrc=faker.isrc(),
        title=faker.title(),
        #audio_file_id=faker.uuid4(),
        # soundrecording?
        owner=user,
        purchase_cost=1,
        stream_cost=0.01,
        ## added
        composition = create_composition(user)
    )
    track.save()
    contributors = [Contributor(artist=artist, role=faker.role()) for artist in artists]
    [contributor.save() for contributor in contributors] # this line is hard to understand why an array ?
    [track.artists.add(contributor) for contributor in contributors] # ditto
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
    contributors = [Contributor(artist=artist, role=faker.role()) for artist in artists]
    [contributor.save() for contributor in contributors]
    [album.artists.add(contributor) for contributor in contributors]
    [album.tracks.add(track) for track in tracks]
    return album

## added create location

def create_location():
    return Location(
    address_one = faker.street_address() , city = faker.city(), country = faker.country()
    )
## added create composition
def create_composition(user):
    return Composition(
    title = faker.title(),
    user = user

    )
