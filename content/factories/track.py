import factory
from faker import Faker

from ..models import Track
from .user import UserFactory
from .contributor import ContributorFactory
from .composition import CompositionFactory
from .providers import TitleProvider, ISRCProvider

faker = Faker()
faker.add_provider(TitleProvider)
faker.add_provider(ISRCProvider)


class TrackFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Track

    isrc = factory.LazyFunction(faker.isrc)
    title = factory.LazyFunction(faker.title)
    owner = factory.SubFactory(UserFactory)
    purchase_cost = 1
    stream_cost = 0.01

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
    def composition(self, create, extracted, **kwargs):
        artists = self.artist_list
        CompositionFactory.create(
            title=self.title, owner=self.owner, artists=artists,
        )
