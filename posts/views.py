"""Posts views."""


#django 
#from django.shortcuts import render
#from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView DetailView CreateView

# froms 
from posts.forms import PostForm
# models
from posts.models import Post


#utilitis
from datetime import datetime



class PostFeedView(LoginRequiredMixin, ListView):
    """Return all pubshiedl post """
    template_name  = 'posts/reed.html'
    model = Post
    ordering = ('-created',)
    paginate_by=2
    context_object_name = 'posts'


class PostDetailView(LoginRequredMixin, DetailView):
    """Return post Detail ."""
    template_name= 'post/detail.html'
    queryset=Post.objects.all()
    context_object_name='posts'

class CreatePostView(LoginRequiredMixin, CreateView):
    """ Create a new post """
    tempalte_name = 'posts/new.html'
    from_class = PostForm
    success_url = reverse_lazy('posts:feed')
    
    def get_context_data(self, **kwargs):
        """Add user and profle to context """
        context = super().get_context_data(**kwargs)
        context['user']= self.request.user
        context['profile']= self.request.user.profile
        return context

