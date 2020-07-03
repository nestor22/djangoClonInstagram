"""POST URLS"""
#django 
from django.urls import path 

from post import views

urlpatterns=[
    path(
        route='',
        view = views.list_posts, 
        name='feed'),
    path(
        route='posts/new/', 
        view=views.create_post, 
        name='create_post'),
]



