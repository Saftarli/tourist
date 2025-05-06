from django.shortcuts import render

from faq.models import FAQ


# Create your views here.
def faq(request):
    context = {
        'faq': FAQ.objects.all(),
    }
    return render(request, 'faq/faq.html', context)