"""Users Urls"""

#django 
from django.urls import path
from users import views


urlpatterns=[
    path(
        route='<str:username>/',
        view=views.UserDetailView.as_view(),
        name='detail'
        ),
        
    path(
        route='users/login/', 
        view=views.login_view, 
        name='login'),
    path(
        route='users/logout/', 
        view=views.logout_view, 
        name='logout'),
    path(
        route='users/singup/', 
        view=views.signup, 
        name='signup'),
    path(
        route='users/me/profile/', 
        view=views.update_profile, 
        name='update_profile'),
        
]
