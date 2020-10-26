import factory
from faker import Faker

from ..models import Contributor
from .artist import ArtistFactory
from .providers import RoleProvider

faker = Faker()
faker.add_provider(RoleProvider)


class ContributorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Contributor

    artist = factory.SubFactory(ArtistFactory)
    role = factory.LazyFunction(faker.role)
