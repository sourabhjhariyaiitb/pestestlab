from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

wagtail_urlpatterns = [
    path('cms/', include(wagtailadmin_urls)),
    path('documents/', include(wagtaildocs_urls)),
    path('pages/', include(wagtail_urls)),
]
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('registration/', include('django.contrib.auth.urls')),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('', include('map.urls')),
    path('', include('forms.urls')),
    path('', include('pwa.urls')),
] + wagtail_urlpatterns
