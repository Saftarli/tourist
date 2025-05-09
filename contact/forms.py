from django import forms
from .models import TourBooking

class TourBookingForm(forms.ModelForm):
    class Meta:
        model = TourBooking
        fields = ['name', 'email', 'phone', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Adınız'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'E-poçt ünvanınız'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+994 XX XXX XX XX'}),
            'subject': forms.Select(attrs={'class': 'form-select nice-select'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Mesajınız'}),
        }
