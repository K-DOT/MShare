from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

AbstractUser._meta.get_field('email')._unique = True
AbstractUser._meta.get_field('email').blank = False

class User(AbstractUser):
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'  
    avatar = models.ImageField(upload_to='profile_images', blank=True)
    about = models.TextField(blank=True)
    show_email_in_profile = models.BooleanField(default=True)
    favorite_materials = models.ManyToManyField('sharing.Material', blank=True)
    def image_tag(self):
        if self.avatar:
            return '<img src="http://127.0.0.1:8000/media/%s/">' % self.avatar
    image_tag.short_description = ''
    image_tag.allow_tags = True

    def get_absolute_url(self):
        return '/users/user/%s/' % self.username

    def __unicode__(self):
        return self.first_name