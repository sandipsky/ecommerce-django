from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/users', null=True, blank=True, default='/static/images/defaultuser.jpg')
    def __str__(self):
        return self.user.username

    @property
    def get_photo_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return "/static/images/defaultuser.jpg"