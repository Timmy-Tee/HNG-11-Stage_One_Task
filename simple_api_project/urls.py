from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("api.urls"))
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = 'api.views.error404'
