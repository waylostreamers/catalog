from random import randint

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError

from content.seed import seed, clear_data

User = get_user_model()


class Command(BaseCommand):
    help = "Finds a random user"

    def handle(self, *args, **options):
        users = User.objects.all()
        count = users.count()
        index = randint(0, count - 1)
        user = users.all()[index]
        print(user)
