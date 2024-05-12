from django.core.management.base import BaseCommand
from shopapp.models import Customer, Products, Orders


class Command(BaseCommand):
    help = "Get all orders by customers id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Customer ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        customer = Customer.objects.filter(pk=pk).first()
        if customer is not None:
            orders = Orders.objects.filter(customer=customer)
            intro = f'All orders of {customer.name}\n'
            ords = '\n'.join(str(order) for order in orders)
            self.stdout.write(f'{intro}{ords}')