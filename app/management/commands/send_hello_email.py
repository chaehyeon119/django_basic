from django.core.management import BaseCommand


class Command(BaseCommand):
    # def add_arguments(self, parser):
    #    super().add_arguments(parser)

    def handle(self, *args, **options):
        print("hello world")
