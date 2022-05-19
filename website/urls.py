from django.urls import path

from . import views

urlpatterns = [
    path('', views.allp, name='all'),
    path('delete/<int:id>', views.delete, name='delete'),
]