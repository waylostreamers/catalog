import logging
from faker import Faker
from django.db import transaction

from ..factories import (
    UserFactory,
    ArtistFactory,
    AlbumFactory,
)
from .. import models

logger = logging.getLogger("seeder")
faker = Faker()

seeded_models = [
    models.Track,
    models.Composition,
    models.Album,
    models.Track,
    models.Contributor,
    models.Artist,
]


@transaction.atomic
def seed(num_users):
    logger.info("Seeding database...")
    users = [UserFactory() for n in range(num_users)]
    for user in users:
        num_artists = faker.random.randint(1, 10)
        num_albums = faker.random.randint(1, 5)
        artists = [ArtistFactory(owner=user) for n in range(num_artists)]
        for album in range(num_albums):
            num_tracks = faker.random.randint(1, 10)
            AlbumFactory.create(owner=user, artists=artists, num_tracks=num_tracks)

    logger.info(f"Generated {len(users)} users with randomized track and album data.")


def clear_data():
    for model in seeded_models:
        logger.info(f"Deleting all {model.__name__} objects...")
        model.objects.all().delete()
    logger.info("Deleted all model data.")
