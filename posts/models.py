"""Post models."""

from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profield = models.ForeignKey('users.Profile', on_delete = models.CASCADE)
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='post/photos')
    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)

    def __str__(self):
        """return user an title """
        return '{} by {}'.format(self.title, self.username)
    