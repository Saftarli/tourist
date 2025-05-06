from django.urls import path
from tour.views import tours,tour_details

urlpatterns = [
    path('', tours, name='tour'),
    path('tour-details/', tour_details, name='tour-details'),
]
