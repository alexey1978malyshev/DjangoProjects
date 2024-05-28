from django.db import models
from django.utils.text import slugify
from django.conf import settings


class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=150)
    registration_date = models.DateField()

    def __str__(self):
        return f'Username: {self.name}, email: {self.email}, phone_number: {self.phone_number}.'


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField()
    added_date = models.DateField()
    image = models.ImageField(upload_to='shopimg')

    def __str__(self):
        return f'Product: {self.name}, price: {self.price}, quantity: {self.quantity}.'



class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)


class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images_created', blank=True)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True)
    url = models.URLField()
    image = models.ImageField(upload_to='images/%Y/%m/%d')
    description = models.TextField(blank=True)
    created = models.DateField(auto_now_add=True, db_index=True)
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            super(Image, self).save(*args, **kwargs)


