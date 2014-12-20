from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from users.forms import AdminUserCreationForm, AdminUserChangeForm
from users.models import User

# Register your models here.
class UserAdmin(BaseUserAdmin):
    form = AdminUserChangeForm
    add_form = AdminUserCreationForm
    readonly_fields = ('image_tag',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (('Personal info'), {'fields': (
            'first_name',
            'last_name',
            'about',
            'email',
            'show_email_in_profile',
            'avatar',
            'image_tag',
            'favorite_materials',
        )}),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'email', 'show_email_in_profile', 'first_name', 'last_name', 'about')}
        ),
    )

admin.site.register(User, UserAdmin)      