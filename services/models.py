from django.db import models
from core.mixins import SeoMixin
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.urls import reverse
# Create your models here.

class Service(SeoMixin, models.Model):
    slug = models.SlugField(unique=True,blank=True)
    cover_title = models.CharField(max_length=100)
    cover_image = models.ImageField(upload_to='services/covers/', null=True, blank=True, help_text='312x274 ölçüdə olacaq şəkil')
    image1 = models.ImageField(upload_to='services/images/', null=True, blank=True, help_text='872x536 ölçüdə olacaq şəkil')
    image2 = models.ImageField(upload_to='services/images/', null=True, blank=True,help_text='872x400 ölçüdə olacaq şəkil')
    title = models.CharField(max_length=100, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    subtitle = models.CharField(null=True, blank=True,max_length=100)
    subcontent = RichTextField(null=True, blank=True)
    gallery_title = models.CharField(max_length=100, null=True, blank=True)
    gallery_image = models.ImageField(upload_to='services/gallery/', null=True, blank=True,help_text='312x215 ölçüdə olacaq şəkil')
    gallery_image1 = models.ImageField(upload_to='services/gallery/', null=True, blank=True,help_text='536x215 ölçüdə olacaq şəkil')
    gallery_image2 = models.ImageField(upload_to='services/gallery/', null=True, blank=True,help_text='536x215 ölçüdə olacaq şəkil')
    gallery_image4 = models.ImageField(upload_to='services/gallery/', null=True, blank=True, help_text='312x215 ölçüdə olacaq şəkil')

    def __str__(self):
        return self.cover_title
    class Meta:
        verbose_name_plural = 'Xidmətlər'

    def get_absolute_url(self):
        return reverse('service_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.cover_title)
        super(Service, self).save(*args, **kwargs)

class ServicesIndex(SeoMixin, models.Model):
    def __str__(self):
        return 'Xidmətlər'

    class Meta:
        verbose_name_plural = 'Xidmətlər Seo'


