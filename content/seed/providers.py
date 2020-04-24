from faker import Faker
from faker.providers import BaseProvider

from ..models import Role

faker = Faker()


class TitleProvider(BaseProvider):
    def title(self):
        length = faker.randomize_nb_elements(3, min=1, max=5)
        return faker.sentence(length)[:-1].title()


class RoleProvider(BaseProvider):
    contributor_roles = ["primary", "featured"]

    def role(self):
        return Role.objects.get(description=faker.random.choice(self.contributor_roles))


class ISRCProvider(BaseProvider):
    prefix = "WAY"

    def isrc(self):
        return f"{self.prefix}{faker.uuid4()[0:9].upper()}"
