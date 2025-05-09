from django.db import models

class TourBooking(models.Model):
    TOUR_CHOICES = [
        ('Saglamliq turu', 'Sağlamlıq turu'),
        ('Xarici tur', 'Xarici tur'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    subject = models.CharField(max_length=50, choices=TOUR_CHOICES)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"
    class Meta:
        verbose_name_plural = 'Contactdan gelen mesajlar'