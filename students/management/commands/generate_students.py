from django.core.management.base import BaseCommand

from students.models import Student


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('count', nargs='?', default=1, type=int)

    def handle(self, *args, **options):
        count = options['count']
        return Student.generate_students(count=count)
