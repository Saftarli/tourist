from django.contrib import admin
from faq.models import FAQ,FaqPageIndex
# Register your models here.

class SingleInstanceAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
        return True
admin.site.register(FAQ, )
admin.site.register(FaqPageIndex, SingleInstanceAdmin)