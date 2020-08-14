from django.urls import path, include
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static
from mainapp import views

app_name = "mainapp"

urlpatterns = [
    path('', views.index, name="index"),
    # path('projects/', include("projects.urls")),
    # path('ckeditor/', include('ckeditor_uploader.urls')),
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)