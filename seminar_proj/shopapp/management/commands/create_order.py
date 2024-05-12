from django.core.management.base import BaseCommand
from shopapp.models import Customer, Product, Order


class Command(BaseCommand):
    help = "Create order by cust_id and prd_id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Customer ID')
        parser.add_argument('prod_id', type=int, help='Product ID')


    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        customer = Customer.objects.filter(id=pk)
        product_id = kwargs.get('prod_id')
        product = Product.objects.filter(id=product_id)
        price = Product(product).price
        order = Order(customer=Customer(customer), products=product_id, total_price=price)
        order.save()
        self.stdout.write(f'{order}')