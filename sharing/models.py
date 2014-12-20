import datetime
from django.db import models
from users.models import User
from taggit.managers import TaggableManager
from django.conf import settings
from django.utils.timezone import now
from tinymce import models as tinymce_models

#now = now()

# Create your models here.


class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    desc = models.TextField(blank=True, help_text='Short description (Optional)')    

    def get_absolute_url(self):
        return '/materials/categories/%s/' % self.slug

    def __str__(self):
        return self.title


class Material(models.Model):
    class Meta:
        verbose_name='Material'
        verbose_name_plural='Materials'
    title = models.CharField(max_length=60)
    desc = tinymce_models.HTMLField(max_length=500, help_text='Short description (Optional)')
    desc_image = models.ImageField(upload_to='img', blank=True, null=True)
    body = tinymce_models.HTMLField()
    
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    category = models.ForeignKey(Category)
    tags = TaggableManager()
    slug = models.SlugField(unique=True)
    pub_date = models.DateTimeField(default=now)

    def get_absolute_url(self):
        return '/materials/%s/%s/%s/%s/' % (
            self.pub_date.strftime("%Y"), 
            self.pub_date.strftime("%B"),
            self.pub_date.strftime("%d"),
            self.slug
        )

    def __str__(self):
        return self.title            