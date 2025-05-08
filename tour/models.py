from django.db import models
from django.db.models import CharField

from core.mixins import SeoMixin
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.

class Tour(SeoMixin):
    slug = models.SlugField(unique=True,blank=True)
    cover_title = models.CharField(max_length=120, )
    cover_image = models.ImageField(upload_to="tour/cover_image", null=True, blank=True,help_text='424x274 ölçüdə olmalıdır şəkil')
    image1 = models.ImageField(upload_to="tour/image", null=True, blank=True)
    image2 = models.ImageField(upload_to="tour/image2", null=True, blank=True)
    image3 = models.ImageField(upload_to="tour/image3", null=True, blank=True)
    title = models.CharField(max_length=120, blank=True)
    content = models.TextField(blank=True)
    subtitle = models.CharField(max_length=120, blank=True)
    subcontent = RichTextField(blank=True)

    def __str__(self):
        return self.cover_title

    class Meta:
        verbose_name_plural = 'Turlar'

    def get_absolute_url(self):
        return reverse('tour_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.cover_title)
        super(Tour, self).save(*args, **kwargs)


class TourIndex(SeoMixin):
    def __str__(self):
        return 'Turlar Seo'

    class Meta:
        verbose_name_plural = 'Turlar Seo'


