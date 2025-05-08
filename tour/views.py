from django.shortcuts import render, get_object_or_404

from tour.models import Tour


# Create your views here.
def tours(request):
    context = {
        'tours': Tour.objects.all(),
    }
    return render(request, 'tour/tour.html')


def tour_details(request, slug):
    context = {
        'tour': get_object_or_404(Tour, slug=slug),
    }
    return  render(request, 'tour/tour-details.html')