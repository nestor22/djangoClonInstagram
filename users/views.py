""" users views"""
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

def login_view(request):
    """ login view."""
    if request.method == 'POST':
        
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('posts')
        else:
            return render(request, 'users/login.html', {'error':'Invalid Username or password'})
    return render(request, 'users/login.html')

def signup(request):
    """ sign up view"""
    return reder(request, 'users/signup.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')



