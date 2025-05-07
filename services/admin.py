from django.contrib import admin

from services.models import Service, ServicesIndex
# Register your models here.
admin.site.register(Service)
admin.site.register(ServicesIndex)