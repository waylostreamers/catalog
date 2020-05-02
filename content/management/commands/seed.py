from django.core.management.base import BaseCommand, CommandError
from content.seed import seed


class Command(BaseCommand):
    help = "Seeds the database with fake data"

    def add_arguments(self, parser):
        parser.add_argument(
            "--users", help="The number of users to generate.", type=int
        )

    def handle(self, *args, **options):
        users = options["users"] or 10

        seed(users=users)
