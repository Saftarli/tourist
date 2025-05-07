from django.contrib import admin
from about.models import About, AboutIndexPage
# Register your models here.
class SingleInstanceAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
        return True

class AboutAdmin(SingleInstanceAdmin):
    pass
admin.site.register(About,SingleInstanceAdmin)
admin.site.register(AboutIndexPage)
