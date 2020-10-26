import factory
from faker import Faker

from .user import UserFactory
from ..models import Artist, Alias

faker = Faker()


class AliasFactory(factory.django.DjangoModelFactory):
    """Don't try to create this without providing
    an artist due to circular dependancy.
    """

    class Meta:
        model = Alias

    name = factory.Faker("name")
    default = False
    artist = factory.SubFactory("content.factories.ArtistFactory")


class ArtistFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Artist

    owner = factory.SubFactory(UserFactory)

    @factory.post_generation
    def alias(self, create, extracted, **kwargs):
        default_alias = AliasFactory(artist=self, default=True)
        if faker.boolean(chance_of_getting_true=25):
            # A small number of artists have a second alias,
            # which is their initials.
            AliasFactory(
                artist=self, name=get_initials(default_alias.name),
            )
        if faker.boolean(chance_of_getting_true=5):
            # An even smaller number fancy themselves as Prince copycats
            default_alias.default = False
            default_alias.save()
            AliasFactory(
                artist=self,
                name=f"The Artist Formerly Known As {default_alias}",
                default=True,
            )


def get_initials(name):
    """
    This function takes a string and replaces
    each word before the last word with its initial.
    For example:
    Johann Sebastian Bach -> J.S. Bach
    """
    names = name.split(" ")
    if len(names) < 2:
        raise ValueError("Cannot create initials for single word name")
    given_names = names[0:-1]
    last_name = names[-1]
    initials = ""
    for name in given_names:
        initials = "".join([initials, f"{name[0].upper()}."])
    initials = "".join([initials, f" {last_name.capitalize()}"])
    return initials
