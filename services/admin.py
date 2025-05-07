from django.contrib import admin
from django.utils.text import slugify
from services.models import Service, ServicesIndex
# Register your models here.

class ServicesIndexAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.slug = slugify(obj.cover_title)
        super().save_model(request, obj, form, change)


admin.site.register(Service)
admin.site.register(ServicesIndex)