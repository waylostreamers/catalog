from faker import Faker
from faker.providers import BaseProvider

from ..models import Roles

faker = Faker()
roles = Roles()


class TitleProvider(BaseProvider):
    def title(self):
        length = faker.randomize_nb_elements(3, min=1, max=5)
        return faker.sentence(length)[:-1].title()


class RoleProvider(BaseProvider):
    choices = [roles.PRIMARY, roles.FEATURED]

    def role(self):
        return faker.random.choice(self.choices)


class ISRCProvider(BaseProvider):
    prefix = "WAY"

    def isrc(self):
        return f"{self.prefix}{faker.uuid4()[0:9].upper()}"


class ISWCProvider(BaseProvider):
    prefix = "WAYCOMP"

    def iswc(self):
        return f"{self.prefix}{faker.uuid4()[0:9].upper()}"
