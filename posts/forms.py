"""Post From  """

from django import forms

from  posts.models import Post

class PostForm(forms.ModelForm):
    model = Post
    fields = ('user', 'profile', 'title', 'photo')
    