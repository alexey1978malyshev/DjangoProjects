import locale
from django.views import View
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView
from django.utils import timezone
from .models import Customer, Product, Order
from .forms import UpdateProdForm, ImageForm, ImageCreateForm
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages



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


def update_prod(request, prod_id: int):
    message = 'Внесите изменения'
    if request.method == 'POST':

        form = UpdateProdForm(request.POST, request.FILES)
        if form.is_valid():
            product = Product()
            product.pk = prod_id
            product.name = form.cleaned_data['name']
            product.description = form.cleaned_data['description']
            product.price = form.cleaned_data['price']
            product.quantity = form.cleaned_data['quantity']
            product.added_date = form.cleaned_data['added_date']
            # image = form.cleaned_data['image']
            # product.image = image
            # fs = FileSystemStorage()
            # fs.save(image.name, image)
            product.save()
            message = f'Продукт: {product}\nизменен'
            #return render(request, 'shopapp/update_prod.html', {'message': message})

    else:
        product = Product.objects.filter(pk=prod_id).first()
        form = UpdateProdForm()
        if product is not None:
            message = f'Внесите необходимые изменения в товар id={product.pk}, наименование - {product.name} '
    return render(request, 'shopapp/update_prod.html', {'form': form, 'message': message})


def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
    else:
        form = ImageForm()
    return render(request, 'shopapp/upload_image.html', {'form': form})


def image_create(request):
    if request.method == 'POST':
        # form is sent
        form = ImageCreateForm(data=request.POST)
        if form.is_valid():
            # form data is valid
            cd = form.cleaned_data
            new_item = form.save(commit=False)

            # assign current user to the item
            new_item.user = request.user
            new_item.save()
            messages.success(request, 'Image added successfully')

            # redirect to new created item detail view
            return redirect(new_item.get_absolute_url())
    else:
        # build form with data provided by the bookmarklet via GET
        form = ImageCreateForm(data=request.GET)
    return render(request, 'shopapp/image/create.html', {'section': 'images', 'form': form})