"""resume URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.views.generic import RedirectView
from django.urls import path, include
from django.conf.urls.static import static
from django.conf.urls import handler404
from mainapp import views as main_views
from django.views.generic.base import TemplateView
import os

handler404 = main_views.myhandler404

urlpatterns = [
    path('', include('mainapp.urls', namespace="mainapp")),
    path('projects/', include("projects.urls", namespace="projects")),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('favicon.ico', RedirectView.as_view(url='/static/img/icon.ico', permanent=True)),
    path("robots.txt", TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.ADMIN_ENABLED:
    urlpatterns += [path(os.environ.get("ADMIN_PATH"), admin.site.urls)]


