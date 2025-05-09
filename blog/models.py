from django.db import models
from core.mixins import SeoMixin
from django.utils.text import slugify
from django.urls import reverse
# Create your models here.
class Blog(SeoMixin):
    slug = models.SlugField(unique=True, blank=True)
    cover_image = models.ImageField(null=True, blank=True)
    cover_title = models.CharField(max_length=100, null=True, blank=True)
    cover_description = models.CharField(max_length=100, null=True, blank=True)
    image1 = models.ImageField(null=True, blank=True, help_text='872x490 olcu olacaq')
    title = models.CharField(max_length=100, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    image2 = models.ImageField(null=True, blank=True, help_text='872x400 olcu olacaq')
    subtitle = models.CharField(max_length=100, null=True, blank=True)
    subcontent = models.CharField(max_length=100, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cover_title
    class Meta:
        verbose_name_plural = 'Xəbərlər'

    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.cover_title)
        super(Blog, self).save(*args, **kwargs)


class BlogIndex(SeoMixin):
    def __str__(self):
        return  'Blog'

    class Meta:
        verbose_name_plural = 'Xəbərlər SEO'