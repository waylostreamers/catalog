import factory
from faker import Faker

from ..models import Album
from .user import UserFactory
from .contributor import ContributorFactory
from .track import TrackFactory
from .providers import TitleProvider

faker = Faker()
faker.add_provider(TitleProvider)


class AlbumFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Album

    upc = factory.LazyFunction(faker.upc_a)
    title = factory.LazyFunction(faker.title)
    artwork_id = factory.Faker("uuid4")
    owner = factory.SubFactory(UserFactory)
    purchase_cost = 10

    @factory.post_generation
    def artists(self, create, extracted, **kwargs):
        self.artist_list = extracted
        if not create:
            return
        if extracted:
            for artist in extracted:
                contributor = ContributorFactory(artist=artist)
                self.contributors.add(contributor)

    @factory.post_generation
    def tracks(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for track in extracted:
                self.tracks.add(track)

    @factory.post_generation
    def num_tracks(self, create, extracted, **kwargs):
        artists = self.artist_list
        if extracted:
            for index in range(extracted):
                track = TrackFactory.create(owner=self.owner, artists=artists)
                self.tracks.add(track)
