from django import forms
from django.utils.text import slugify
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from tinymce.widgets import TinyMCE
from sharing.models import Material
from users.models import User

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['title', 'desc', 'body', 'category', 'tags']
        exclude = ['author']
    slug = forms.SlugField(required=False)    
    desc = forms.CharField(max_length = 500, widget = TinyMCE(attrs={'cols': 90, 'rows': 20}), required=False)
    body = forms.CharField(widget = TinyMCE(attrs={'cols': 90, 'rows': 20}), required=True)
    
    def clean_slug(self):
        slug = slugify(self.cleaned_data['title'])
        try:
            exsists = Material.objects.get(slug=slug) 
        except Material.DoesNotExist:
            exsists = False     
        if exsists:
            raise ValidationError('Autogeneration failed. Slug must be unique!')

    def save(self, **kwargs):
        instance = super(MaterialForm, self).save(commit=False)
        instance.slug = slugify(instance.title)
        instance.user = self.cleaned_data.get('user')
        try:
            instance.save()
        except IntegrityError:
            return
        return instance     