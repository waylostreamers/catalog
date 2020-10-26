import factory
from faker import Faker

from ..models import Composition, Roles
from .user import UserFactory
from .contributor import ContributorFactory
from .providers import TitleProvider, ISWCProvider

roles = Roles()
faker = Faker()
faker.add_provider(TitleProvider)
faker.add_provider(ISWCProvider)


class CompositionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Composition

    iswc = factory.LazyFunction(faker.iswc)
    title = factory.LazyFunction(faker.title)
    owner = factory.SubFactory(UserFactory)

    @factory.post_generation
    def artists(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for artist in extracted:
                contributor = ContributorFactory(artist=artist, role=roles.COMPOSER)
                self.contributors.add(contributor)
