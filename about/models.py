from django.db import models
from core.mixins import SeoMixin

# Create your models here.
class About(SeoMixin, models.Model):
    image1 = models.ImageField(upload_to='about/images/', null=True, blank=True)
    image2 = models.ImageField(upload_to='about/images/', null=True, blank=True)
    image3 = models.ImageField(upload_to='about/images/', null=True, blank=True)
    title = models.CharField(max_length=120, null=True, blank=True)
    content = models.TextField(blank=True, null=True)
    subtitle1 = models.CharField(max_length=120, null=True, blank=True)
    subcontent1 = models.TextField(blank=True, null=True)
    subtitle2 = models.CharField(max_length=120, null=True, blank=True)
    subcontent2 = models.TextField(blank=True, null=True)
    subtitle3 = models.CharField(max_length=120, null=True, blank=True)
    subcontent3 = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Haqqımızda'


class AboutIndexPage(SeoMixin, models.Model):
    def __str__(self):
        return 'Haqqımızda Seo'
    class Meta:
        verbose_name_plural = 'Haqqımızda Seo'