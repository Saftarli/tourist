from django.contrib import admin
from core.models import SiteSettings
# Register your models here.

class SingleInstanceAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
        return True


class SiteSettingsAdmin(SingleInstanceAdmin):
    pass
admin.site.register(SiteSettings,SingleInstanceAdmin)