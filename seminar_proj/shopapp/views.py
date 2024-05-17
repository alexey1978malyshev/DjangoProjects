import locale
from django.views import View
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView
from django.utils import timezone
from .models import Customer, Product, Order


def index(request):
    context = {"name": "Alexey"}
    return render(request, 'shopapp/index.html', context)


def about(request):
    birth_year = 1978
    context = {"age": (timezone.datetime.now().year - birth_year),
               "educ": "высшее",
               "country": locale.getlocale()[0].split('_')[-1],
               "last_sym_age": (timezone.datetime.now().year - 1978) % 10,
               }
    return render(request, "shopapp/about.html", context)


def get_orders_by_customers_id(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    if customer is not None:
        orders = Order.objects.filter(customer=customer)
        context = {'name': f'All orders of {customer.name}\n',
                   'orders': orders,
                   }
        return render(request, "shopapp/orders_info.html", context)


def get_products(request, customer_id: int):
    customer = get_object_or_404(Customer, pk=customer_id)
    if customer is not None:
        week_orders = Order.objects.filter(customer=customer).order_by('-date_ordered')[:7]
        month_orders = Order.objects.filter(customer=customer).order_by('-date_ordered')[:30]
        year_orders = Order.objects.filter(customer=customer).order_by('-date_ordered')[:365]
        context = {'week_orders': week_orders, 'month_orders': month_orders, 'year_orders': year_orders}
        return render(request, "shopapp/orders_by_time.html", context)
