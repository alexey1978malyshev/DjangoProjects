from django.core.management.base import BaseCommand
from myapp2.models import User
from faker import Faker
from random import randint

fake = Faker()


class Command(BaseCommand):
    help = "Create user."

    def handle(self, *args, **kwargs):
        user = User(name=fake.name(), email=fake.email(), password=fake.password(), age=randint(12, 112))

        user.save()
        self.stdout.write(f'{user}')
