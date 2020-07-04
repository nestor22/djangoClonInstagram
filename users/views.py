""" users views"""
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.view.generic import DetailView
# Exeptions
from django.db.utils import IntegrityError
#models
from django.contrib.auth.models import User
from users.models import Profile

# Forms
from users.forms import Profileform, SigupForm


class UserDataView(DetailView):
    """User detail  vioew"""
    template_name = 'users/detail.html'
    slug_file = 'username'
    slug_url = 'username'
    queryset = User.objects.all()

    



@login_required
def update(request):
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

            return redirect('users:update')

        else:
            form = Profileform()

    
    return render(
        request = request,
        template_name = 'users/update.html',
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
            return redirect('posts:feed')
        else:
            return render(request, 'users/login.html', {'error':'Invalid Username or password'})
    return render(request, 'users/login.html')



def signup(request):
    """sign up view"""
    if request.method == 'POST':
        form =  SigupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user:login')
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
    return redirect('user:login')



