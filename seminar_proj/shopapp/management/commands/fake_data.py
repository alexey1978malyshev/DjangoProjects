from django.core.management.base import BaseCommand
from shopapp.models import Customer, Product, Order
from faker import Faker
from random import randint


class Command(BaseCommand):
    help = "Generate fake customers  products and orders."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Quantity fake notes')

    def handle(self, *args, **kwargs):
        fake = Faker()

        count = kwargs.get('count')
        for i in range(count):
            customer = Customer(name=fake.name(), email=fake.email(), phone_number=fake.phone_number(),
                                address=fake.address(), registration_date=fake.date_this_year())
            customer.save()

            product = Product(name=fake.word(), description=fake.text(max_nb_chars=120), price=randint(100, 9999),
                              quantity=randint(1, 500), added_date=fake.date_this_year())
            product.save()


