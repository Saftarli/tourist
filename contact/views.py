from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import TourBookingForm

def contact(request):
    if request.method == 'POST':
        form = TourBookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Mesajınız uğurla göndərildi!")
            return redirect('contact')
    else:
        form = TourBookingForm()

    return render(request, 'contact/contact.html', {'form': form})
