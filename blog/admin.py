from django.contrib import admin
from django.utils.text import slugify
from blog.models import Blog, BlogIndex


# Register your models here.
class BlogIndexAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.slug = slugify(obj.cover_title)
        super().save_model(request, obj, form, change)


admin.site.register(Blog)
admin.site.register(BlogIndex, BlogIndexAdmin)

