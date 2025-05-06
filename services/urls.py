from django.urls import path
from services.views import  services,service_detail


urlpatterns = [
    path('', services, name='services'),
    path('services-details/', service_detail, name='service-details'),

]