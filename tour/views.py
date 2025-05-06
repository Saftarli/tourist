from django.shortcuts import render

# Create your views here.
def tours(request):
    return render(request, 'tour/tour.html')
def tour_details(request):
    return  render(request, 'tour/tour-details.html')