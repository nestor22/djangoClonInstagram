"""Posts views."""


#django 
#from django.shortcuts import render
#from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
# froms 
from posts.forms import PostForm
# models
from posts.models import Post


#utilitis
from datetime import datetime


@login_required
def list_posts(request):
    """list existing posts. """
    posts = Post.objects.all().order_by('-created')
    return render(request,'posts/feed.html', { 'posts':posts})

@login_required
def create_post(request):
    if request.methon == 'POST':
        from=PostForm(request.POST, request.FILES)
        if form.is_valid:
            form.saver()
            return  redirect('feed')
    else:
        form = PostForm()


    return render(
        request = request, 
        template_name = 'posts/new.html',
        context={
            'form': form,
            'user'; request.user,
            'profile': request.user.profile
        }
    )

