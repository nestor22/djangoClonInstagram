"""Posts views."""


#django 
#from django.shortcuts import render
#from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

# froms 
from posts.forms import PostForm
# models
from posts.models import Post


#utilitis
from datetime import datetime


class PostFeedView(LoginRequredMixin, DetailView):
    """Return post Detail ."""
    template_name= 'post/detail.html'
    queryset=Post.objects.all()
    context_object_name='posts'


class PostFeedView(LoginRequiredMixin, ListView):
    """Return all pubshiedl post """
    template_name  = 'posts/reed.html'
    model = Post
    ordering = ('-created',)
    paginate_by=2
    context_object_name = 'posts'



@login_required
def create_post(request):
    if request.methon == 'POST':
        form=PostForm(request.POST, request.FILES)
        if form.is_valid:
            form.saver()
            return  redirect('posts:feed')
    else:
        form = PostForm()


    return render(
        request = request, 
        template_name = 'posts/new.html',
        context={
            'form': form,
            'user': request.user,
            'profile': request.user.profile
        }
    )

