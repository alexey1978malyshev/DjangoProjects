from django.shortcuts import render
from faker import Faker
from blogapp.models import Author
from django.http import HttpResponse

fake = Faker()


def index(request):
    return HttpResponse("It's index page")


def create_author(request):
    author = Author(first_name=fake.first_name(), last_name=fake.last_name(), email=fake.email(),
                    biography=fake.text(max_nb_chars=150), birthday=fake.date_of_birth(minimum_age=12, maximum_age=85))
    author.save()
    return HttpResponse(f'Автор <h3>{author}</h3> добавлен в базу')
