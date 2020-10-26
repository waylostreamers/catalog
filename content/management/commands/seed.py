from django.core.management.base import BaseCommand, CommandError
from content.seed import seed, clear_data


class Command(BaseCommand):
    help = "Seeds the database with fake data"

    def add_arguments(self, parser):
        parser.add_argument(
            "--users", help="The number of users to generate.", type=int
        )
        parser.add_argument(
            "--clear",
            help="Set this flag to delete all model data.",
            action="store_true",
        )

    def handle(self, *args, **options):
        users = options["users"] or 10
        clear = options["clear"]
        if clear:
            clear_data()
        else:
            seed(users)
