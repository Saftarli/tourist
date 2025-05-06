
from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('about/',include('about.urls')),
    path('contact/',include('contact.urls')),
    path('services/',include('services.urls')),
    path('tours/',include('tour.urls')),
    path('faq/',include('faq.urls')),
    path('blog/',include('blog.urls')),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)