# from django.conf.urls import url
from django.urls import re_path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    re_path('', views.index, name="index"),
    re_path("search", views.search, name="search_results"),
    re_path("browse", views.browse, name="browse"),
    re_path("location", views.location_filter, name="location"),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
