""" Platzigram View."""
#Django
from django.http import HttpResponse
#Utilitis
from datetime import datetime
import json



def hello_world(request):
    """Return a greeting."""
    now = datetime.now().strftime('%b %dth, - %H:%M hrs')
    return HttpResponse('ho, hi current server time is {noew}'.format(now = str(now)))

def sorted_ints(request):
    """Hi"""
    #numbers = request.GET['numbers']
    numbers =[int(i) for i in request.GET['numbers'].split(',') ]
    sorted_ints = sorted(numbers)
    data = {
        'status':'ok',
        'numbers':sorted_ints,
        'message':'Integers sorted successfully. '
    }
    return HttpResponse(json.dumps(data, indent=4), content_type = 'application/json')


def say_hi(request, name, edad):
    """return a greeting."""
    if edad < 12:
        message = 'sorry{}, you not allowed here'.format(name)
    else:
        message = 'hi {}, welcome to paltzigram'.format(name)
    return HttpResponse(message)