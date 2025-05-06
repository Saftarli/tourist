from django.shortcuts import render

# Create your views here.
def services(request):
    return render(request, 'service/service.html')

def service_detail(request,):
    return render(request, 'service/service-details.html')

