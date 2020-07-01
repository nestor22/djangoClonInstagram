"""Post From  """

from django import forms

from  post.models import posts

class PostForm(forms.ModelForm):
    model = Post
    fields = ('user', 'profile', 'title', 'photo')
    