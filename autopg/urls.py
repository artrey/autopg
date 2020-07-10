from django.urls import path

from .views import create_database_view

urlpatterns = [
    path('', create_database_view, name='create_database'),
]
