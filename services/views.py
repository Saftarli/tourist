from django.shortcuts import render,get_object_or_404

from services.models import Service


# Create your views here.
def services(request):
    context = {
        'services': Service.objects.all(),
    }
    return render(request, 'service/service.html',context)

def service_detail(request,slug):
    context = {
        'service': get_object_or_404(Service, slug=slug),
    }
    return render(request, 'service/service-details.html', context)

