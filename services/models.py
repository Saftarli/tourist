from django.db import models
from core.mixins import SeoMixin
from ckeditor.fields import RichTextField

# Create your models here.

class Service(SeoMixin, models.Model):
    cover_title = models.CharField(max_length=100)
    cover_image = models.ImageField(upload_to='services/covers/', null=True, blank=True)
    image1 = models.ImageField(upload_to='services/images/', null=True, blank=True)
    image2 = models.ImageField(upload_to='services/images/', null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    subtitle = models.TextField(null=True, blank=True)
    subcontent = RichTextField(null=True, blank=True)
    gallery_title = models.CharField(max_length=100, null=True, blank=True)
    gallery_image = models.ImageField(upload_to='services/gallery/', null=True, blank=True)
    gallery_image1 = models.ImageField(upload_to='services/gallery/', null=True, blank=True)
    gallery_image2 = models.ImageField(upload_to='services/gallery/', null=True, blank=True)
    gallery_image4 = models.ImageField(upload_to='services/gallery/', null=True, blank=True)

    def __str__(self):
        return self.cover_title
    class Meta:
        verbose_name_plural = 'Xidmətlər'

class ServicesIndex(SeoMixin, models.Model):
    def __str__(self):
        return 'Xidmətlər'

    class Meta:
        verbose_name_plural = 'Xidmətlər Seo'


