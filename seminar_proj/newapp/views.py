from django.http import HttpResponse
from django.utils import timezone
from random import randint, choice
import logging
from newapp.models import Results
from django.shortcuts import render, get_object_or_404

logger = logging.getLogger(__name__)


# def orel_reshka(request):
#     result = choice(['Орел!!!', 'Решка!'])
#     res = Results(result=result)
#     res.save()
#     return HttpResponse(str(result))

def orel_reshka(request):
    result = choice(['Орел!!!', 'Решка!'])
    res = Results(result=result)
    res.save()
    context = {'name': 'orel_reshka',
               'result': Results.last_val(), }
    return render(request, 'newapp/index.html', context)


# def cube(request):
#     result = randint(1, 6)
#     return HttpResponse(f'Значение одной из шести граней игрального кубика= {result}')

def cube(request, count: int):
    result = [randint(1, 6) for _ in range(count)]
    context = {'name': 'cube',
               'result': result, }
    return render(request, 'newapp/index.html', context)


def random_num(request):
    result = randint(0, 100)
    return HttpResponse(f'Случайное число от 0 до 100= {result}')


def get_last_val(request):
    val = Results.last_val()
    s = '</br>'.join(str(v) for v in val)
    return HttpResponse(s)
