"""Posts views."""


#django 
#from django.shortcuts import render
from django.http import HttpResponse
#utilitis
from datetime import datetime
# Create your views here.
posts =[
    { 
        'name':'Mont Black',
        'user':'Yessica cortes',
        'timestamp':datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture':'https://picsum.photos/200/200/?image=1036', 
    
    },
    { 
        'name':'Via lactea',
        'user':'c Vander',
        'timestamp':datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture':'https://picsum.photos/200/200/?image=1036', 
    
    },
    { 
        'name':'nuevo auditorio',
        'user':'Thepiramitist cortes',
        'timestamp':datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture':'https://picsum.photos/200/200/?image=1036', 
    
    }
]


def list_posts(request):
    """list existing posts. """
   
    content = []
    for post in posts:
        content.append("""
            <p><strong>{name}</strong></p>
            <p><small>{user} - <i>{timestamp}</i></small></p>
            <figure><img src="{picture}"/></figure>
        """.format(**post))
    return HttpResponse('<br>'.join(content))