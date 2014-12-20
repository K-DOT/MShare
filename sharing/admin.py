from django.contrib import admin
from sharing.models import Material, Category

# Register your models here.
class MaterialAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug" : ("title",)}
    class Media:
        js = (
            '/static/tiny_mce/tiny_mce.js',
            '/static/textareas.js',
        )
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'author':
            kwargs['initial'] = request.user.id
        return super(MaterialAdmin, self).formfield_for_foreignkey(
            db_field, request, **kwargs
        )

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug" : ("title",)}
  
admin.site.register(Material, MaterialAdmin)
admin.site.register(Category, CategoryAdmin)