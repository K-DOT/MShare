from users.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class AdminUserCreationForm(UserCreationForm):
    class Meta:
        email = {
            'required': True
        }
        model = User
        fields = ['username', 'password', 'email', 'show_email_in_profile', 'first_name', 'last_name', 'about']

    def clean_username(self):
        username = self.cleaned_data['username']    
        try:
            User._default_manager.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(self.messages['duplicate_username'])      

class AdminUserChangeForm(UserChangeForm):
    class Meta:
        model = User    
        fields = ['username', 'password', 'email', 'show_email_in_profile', 'first_name', 'last_name', 'about']