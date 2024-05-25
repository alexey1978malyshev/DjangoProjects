from django.shortcuts import render
from faker import Faker
from blogapp.models import Author
from django.http import HttpResponse
from .forms import AddNewAuthor

fake = Faker()


def index(request):
    return HttpResponse("It's index page")


def create_author(request):
    author = Author(first_name=fake.first_name(), last_name=fake.last_name(), email=fake.email(),
                    biography=fake.text(max_nb_chars=150), birthday=fake.date_of_birth(minimum_age=12, maximum_age=85))
    author.save()
    return HttpResponse(f'Автор <h3>{author}</h3> добавлен в базу')


def delete_author_by_id(request, id_author: int):
    author = Author.objects.filter(pk=id_author).first()
    if author is not None:
        author.delete()
    return HttpResponse(f'Автор <h3>{author}</h3> удален')


def create_author_by_form(request):
    if request.method == 'POST':
        form = AddNewAuthor(request.POST)
        message = 'Заполнение данных нового автора'
        if form.is_valid():
            author = Author(first_name=form.cleaned_data['first_name'], last_name=form.cleaned_data['last_name'],
                            email=form.cleaned_data['email'], biography=form.cleaned_data['biography'],
                            birthday=form.cleaned_data['birthday'])
            author.save()
            form = AddNewAuthor()
            message = f'Новый автор: {author}\nдобавлен в базу'
    else:
        form = AddNewAuthor()
        message = 'Введите данные автора!'
    return render(request, 'blogapp/add_author.html', {'form': form, 'message': message})
