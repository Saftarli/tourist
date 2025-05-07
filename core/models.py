from django.db import models

# Create your models here.
from django.db import models



# Create your models here.
class SiteSettings(models.Model):
    company_name = models.CharField(max_length=100, null=True, blank=True)
    logo_navbar = models.FileField(upload_to='core/site_settings',
                                   null=True, blank=True)

    logo_navbar_alt_data = models.CharField(max_length=255, null=True, blank=True,
                                            help_text='Add data for increasing SEO performance')

    logo_footer = models.FileField(upload_to='core/site_settings',
                                   null=True, blank=True)
    footer_title = models.CharField(max_length=255, null=True, blank=True)
    footer_subtitle = models.CharField(max_length=255, null=True, blank=True)

    logo_footer_alt_data = models.CharField(max_length=255, null=True, blank=True,
                                            help_text='Add data for increasing SEO performance')

    favicon = models.FileField(upload_to='core/site_settings', null=True, blank=True)
    favicon_alt_data = models.CharField(max_length=255, null=True, blank=True,
                                        help_text='Add data for increasing SEO performance')

    address = models.CharField(max_length=255, null=True, blank=True)
    longitude = models.DecimalField(max_digits=17, decimal_places=15, null=True, blank=True)
    latitude = models.DecimalField(max_digits=17, decimal_places=15, null=True, blank=True)
    iframe = models.TextField(help_text="Just paste iframe src data from googlemap", null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=255, null=True, blank=True,
                                    help_text='Enter phone number starting with the code')

    fax = models.CharField(max_length=255, null=True, blank=True,
                                    help_text='Enter fax number starting with the code')

    facebook = models.URLField(max_length=255, null=True, blank=True, help_text='Enter your facebook url')
    instagram = models.URLField(max_length=255, null=True, blank=True, help_text='Enter your instagram url')
    twitter = models.URLField(max_length=255, null=True, blank=True, help_text='Enter your twitter url')
    linkedin = models.URLField(max_length=255, null=True, blank=True, help_text='Enter your linkedin url')
    youtube = models.URLField(max_length=255, null=True, blank=True, help_text='Enter your youtube url')
    website = models.URLField(max_length=255, null=True, blank=True, help_text='Enter your website url')


    def __str__(self):
        return self.company_name
    class Meta:
        verbose_name_plural = "Sayt Tənzimləmələri"


