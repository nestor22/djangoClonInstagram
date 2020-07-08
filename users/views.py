""" users views"""
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import DetailView, FormView
from django.urls import reverse, reverse_lazy 
# Exeptions
from django.db.utils import IntegrityError
#models
from django.contrib.auth.models import User
from users.models import Profile
from post.models import Post

# Forms
from users.forms import Profileform, SigupForm


class UserDetailView(LoginRequireMixin, DetailView):
    """User detail  view"""
    template_name = 'users/detail.html'
    slug_filed = 'username'
    slug_url_kwarg = 'username'
    queryset = User.objects.all()
    context_object = 'user'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['post'] = Post.objects.filter(user=user).order_by('-created')
        return context
    
class SignupView(FromView):
    template_name = 'users/signup.html'
    from_class = SigunForm
    succes_url = reverse_lazy('users:login')



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
            profile.biograpy = data['biograpy']
            profile.picture = data['picture']
            profile.save()
            url = reverse('users:detail', kwargs{'username':request.user.username})
            return redirect(url)

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






@login_required
def logout_view(request):
    logout(request)
    return redirect('user:login')



