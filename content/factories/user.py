import factory

from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

user_password = "password"


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    email = factory.Faker("email")
    username = factory.LazyAttribute(lambda o: f"{o.email}")
    password = make_password(user_password)
    is_active = True
