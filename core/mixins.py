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

    og_title = models.CharField(max_length=250, blank=True, null=True)
    og_description = models.CharField(max_length=250, blank=True, null=True)
    og_image = models.ImageField(upload_to="seo/", blank=True, null=True, help_text='1200*630')

    twitter_title = models.CharField(max_length=250, blank=True, null=True)
    twitter_description = models.CharField(max_length=250, blank=True, null=True)
    twitter_image = models.ImageField(upload_to="seo/", blank=True, null=True, help_text='800*800')

    canonical_url = models.URLField(blank=True, null=True)
    ROBOTS_CHOICES = [("index, follow", "index, follow"),
                      ("noindex, follow", "noindex, follow"),
                      ("noindex, nofollow", "noindex, nofollow"), ]

    robots_directive = models.CharField(max_length=50, choices=ROBOTS_CHOICES,
                                        default="index, follow", blank=True, null=True)

    schema_json_ld = models.TextField(blank=True, null=True,
                                      help_text="Schema.org üçün JSON formatında structured data əlavə edin.")

    hreflang_links = models.TextField(blank=True, null=True)
    fb_app_id = models.CharField(max_length=100, blank=True, null=True)
    fb_page_url = models.URLField(blank=True, null=True)

    class Meta:
        abstract = True