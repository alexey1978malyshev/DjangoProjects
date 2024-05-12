from django.core.management.base import BaseCommand
from myapp2.models import User


class Command(BaseCommand):
    help = "Update user name by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')
        parser.add_argument('name', type=str, help='User name')
        parser.add_argument('age', type=int, help='User age')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        name = kwargs.get('name')
        age = kwargs.get('age')
        user = User.objects.filter(pk=pk).first()
        user.name = name
        user.age = age
        user.save()
        self.stdout.write(f'{user}')