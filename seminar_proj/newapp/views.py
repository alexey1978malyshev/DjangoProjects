from django.http import HttpResponse
from django.utils import timezone
from random import randint, choice
import logging
from newapp.models import Results
from django.shortcuts import render, get_object_or_404
from .forms import ChoiceGameForm

logger = logging.getLogger(__name__)

def index(request):

    return render(request, 'newapp/index.html')

# def orel_reshka(request):
#     result = choice(['Орел!!!', 'Решка!'])
#     res = Results(result=result)
#     res.save()
#     return HttpResponse(str(result))

def orel_reshka(request, count: int):
    result = [choice(['Орел!!!', 'Решка!']) for _ in range(count)]
    for res in result:
        res_to_db = Results(result=res)
        res_to_db.save()
    context = {'name': 'orel_reshka',
            #   'result': Results.last_val(), }
               'result': result }
    return render(request, 'newapp/index.html', context)


# def cube(request):
#     result = randint(1, 6)
#     return HttpResponse(f'Значение одной из шести граней игрального кубика= {result}')

def cube(request, count: int):
    result = [randint(1, 6) for _ in range(count)]
    context = {'name': 'cube',
               'result': result, }
    return render(request, 'newapp/index.html', context)


def random_num(request, count: int):
    result = [randint(0, 100) for _ in range(count)]
    context = {'name': 'random_num',
               'result': result, }
    return render(request, 'newapp/index.html', context)


def get_last_val(request):
    val = Results.last_val()
    s = '</br>'.join(str(v) for v in val)
    return HttpResponse(s)

def choice_game(request):
    if request.method == 'POST':
        form = ChoiceGameForm(request.POST)
        message = 'Выбери игру!'
        if form.is_valid():
            game = form.cleaned_data['game_choice']
            attempt_quantity = form.cleaned_data['attempt_quantity']
            if game == 'orel_reshka':
                return orel_reshka(request,attempt_quantity)
            if game == 'cube':
                 return cube(request, attempt_quantity)
            if game == 'random_num':
                return random_num(request, attempt_quantity)
            #game(request, attempt_quantity)
            message = f'Выбрана игра {game}!'
    else:
        form = ChoiceGameForm()
        message = 'Выбери игру!'
    return render(request, 'newapp/choice_form.html', {'form': form, 'message': message})

