from django.urls import path

from . import views

app_name = 'resources_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('section/<int:section_id>', views.section, name='section'),
]
