"""platzigram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Ad   d a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

""" nuestros import"""
from platzigram import views as local_views
from posts import views as posts_views
from users import views as user_views




urlpatterns = [
    path('hello-word/', local_views.hello_world, name = 'hello_world'),
    path('admin/', admin.site.urls, ),
    path('sorted/', local_views.sorted_ints, name='sort'),
    path('hi/<str:name>/<int:edad>.', local_views.say_hi, name= 'hi'),
    path('',posts_views.list_posts, name='posts'),
    path('posts/new/', posts_views.create_post, name='create_post'),
    path('users/login/', user_views.login_view, name='login'),
    path('users/logout/', user_views.logout_view, name='logout'),
    path('users/singup/', user_views.signup, name='signup'),
    path('users/me/profile/', user_views.update_profile, name='update_profile'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 


