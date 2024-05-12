from django.core.management.base import BaseCommand
from shopapp.models import Customer
from faker import Faker
from random import randint

fake = Faker()


class Command(BaseCommand):
    help = "Create customer."

    def handle(self, *args, **kwargs):
        customer = Customer(name=fake.name(), email=fake.email(), phone_number=fake.phone_number(),
                            address=fake.address(), registration_date=fake.date_this_year())
        customer.save()
        self.stdout.write(f'{customer}')
