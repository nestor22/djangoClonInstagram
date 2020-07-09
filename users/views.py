""" users views"""
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views
from django.shortcuts import render, redirect
from django.views.generic import DetailView, FormView, UpdateView
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

    def form_falid(self, form):
        """ save from data."""
        form.save()
        return super().form_valid(form)



class UpdateProfileView(LoginRequiredMixin, UpdateView):
    template_name = 'users/update_profile.html'
    model = Profile 
    fields = ['website', 'biograpy', 'phone_number', 'picture']

    def get_ogject(self):
        return self.request.user.prfile

    def get_success_url(self):
        """ return to users profile """
        username = self.object.user.username
        return reverse('users:detail', kwargs = {'username': username})
        
class LoginView(auth_views.LoginView):
    """ logiin view"""
    template_name = 'users/login.html'



class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    """ logout view"""
    tempalte_name = 'users/logged_out.html'





