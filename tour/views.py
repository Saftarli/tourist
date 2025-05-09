from django.shortcuts import render, get_object_or_404
from tour.models import Tour
from django.core.paginator import Paginator


# Create your views here.
def tours(request):
    tour_list = Tour.objects.all()
    paginator = Paginator(tour_list, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'tours': page_obj,
        'page_obj': page_obj,

    }
    return render(request, 'tour/tour.html',context)


def tour_details(request, slug):
    context = {
        'tour': get_object_or_404(Tour, slug=slug),
    }
    return  render(request, 'tour/tour-details.html',context)