from django.shortcuts import render

from about.models import About


# Create your views here.
def about(request):
    context = {
        'about': About.objects.last(),
    }
    return render(request, 'about/about.html', context)