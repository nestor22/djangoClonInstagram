""" users views"""
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
# Exeptions
from django.db.utils import IntegrityError
#models
from django.contrib.auth.models import User
from users.models import Profile

# Forms
from users.forms import Profileform, SigupForm


@login_required
def update_profile(request):
    """updadate a user's profile view"""

    profile = request.user.profile 

    if request.method =='POST':
        form = Profileform(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            profile.website = data['website']
            profile.phone_number = data['phone_number']
            profile.biograpy = data['biography']
            profile.picture = data['picture']

            return redirect('update_profile')

        else:
            form = Profileform()

    
    return render(
        request = request,
        template_name = 'users/update_profile.html',
        context={
            'profile': profile,
            'user': request.user,
            'form': form
        }
    )

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
    """sign up view"""
    if request.method == 'POST':
        form =  SigupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SigupForm()

    return render(
        request = request,
        template_name = 'users/signup.html',
        context = {
            'form':form
        }
    )




@login_required
def logout_view(request):
    logout(request)
    return redirect('login')



