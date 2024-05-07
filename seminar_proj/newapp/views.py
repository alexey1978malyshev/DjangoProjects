from django.http import HttpResponse
from random import randint
import logging


logger = logging.getLogger(__name__)


def orel_reshka(request):
    result = randint(0, 1)
    if result == 0:
        return HttpResponse('Решка!')
    return HttpResponse('Орел!!!')


def cube(request):
    result = randint(1, 6)
    return HttpResponse(f'Значение одной из шести граней игрального кубика= {result}')


def random_num(request):
    result = randint(0, 100)
    return HttpResponse(f'Случайное число от 0 до 100= {result}')
