from django.db import models
from core.mixins import SeoMixin
# Create your models here.
class FAQ(models.Model):
    question = models.TextField(null=False, blank=False)
    answer = models.TextField(null=True, blank=True)
    published = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Suallar"

    def __str__(self):
        return self.question

class FaqPageIndex(SeoMixin):
    def __str__(self):
        return 'Suallar SEO'
    class Meta:
        verbose_name_plural = 'Suallar Seo'