from django.urls import path, include
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static
from mainapp import views

urlpatterns = [
    path('', views.index, name="index"),
    path('projects/', include("projects.urls")),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# serving media files only on debug mode
# if settings.DEBUG:
#     urlpatterns += [
#         path(r'^media/(?P<path>.*)$', serve, {
#             'document_root': settings.MEDIA_ROOT
#         }),
#     ]
#     print(urlpatterns)