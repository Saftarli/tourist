from django.urls import path
from tour.views import tours,tour_details

urlpatterns = [
    path('', tours, name='tour'),
    path('<slug:slug>', tour_details, name='tour-details'),
]
