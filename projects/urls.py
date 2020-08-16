from django.urls import path, include
from projects import views

app_name = 'projects'

urlpatterns = [
    path("<int:id>/", views.project_description, name='description')
]