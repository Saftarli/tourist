from core.models import  SiteSettings
from services.models import Service


def navbar_footer_menu(request):

    context = {
        'site_settings': SiteSettings.objects.last() if SiteSettings.objects.last() else None,

        'services': Service.objects.all(),
    }

    return context