from django.shortcuts import render
from django.http import HttpResponse
import random as rnd
import logging


logger = logging.getLogger(__name__)


def heads_or_tails(request):
    res = rnd.choice(['орел', 'решка'])
    text = f'Результат подбрасывания монетки: {res}'
    logger.info(text)
    return HttpResponse(text)


def dice(request):
    res = rnd.randint(1, 6)
    text = f'Результат шестигранного кубика: {res}'
    logger.info(text)
    return HttpResponse(text)


def random_num(request):
    res = rnd.randint(0, 100)
    text = f'Случайное число от 0 до 100: {res}'
    logger.info(text)
    return HttpResponse(text)
