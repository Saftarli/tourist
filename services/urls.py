from django.urls import path
from services.views import  services,service_detail


urlpatterns = [
    path('', services, name='services'),
    path('<slug:slug>', service_detail, name='service_detail'),

]