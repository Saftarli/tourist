from django.shortcuts import render

from services.models import Service


# Create your views here.
def services(request):
    context = {
        'services': Service.objects.all(),
    }
    return render(request, 'service/service.html',context)

def service_detail(request,):
    return render(request, 'service/service-details.html')

