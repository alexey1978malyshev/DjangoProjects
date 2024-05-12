from django.core.management.base import BaseCommand
from shopapp.models import Customer


class Command(BaseCommand):
    help = "Update customer name by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')
        parser.add_argument('name', type=str, help='User name')
        parser.add_argument('email', type=str, help='User email')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        name = kwargs.get('name')
        email = kwargs.get('email')
        customer = Customer.objects.filter(pk=pk).first()
        customer.name = name
        customer.email = email
        customer.save()
        self.stdout.write(f'{customer}')