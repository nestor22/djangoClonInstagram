""" Platzigram View."""
#Django
from django.http import HttpResponse
#Utilitis
from datetime import datetime


def hello_world(request):
    """Return a greeting."""
    now = datetime.now().strftime('%b %dth, - %H:%M hrs')
    return HttpResponse('ho, hi current server time is {noew}'.format(now = str(now)))

def hi(request):
    """Hi"""
    return HttpResponse('HI')