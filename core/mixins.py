from django.db import models


#
class DateMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

#
class SeoMixin(models.Model):
    head_title = models.CharField(max_length=250, blank=True, null=True)
    meta_description = models.CharField(max_length=250, blank=True, null=True)
    meta_keywords = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        abstract = True