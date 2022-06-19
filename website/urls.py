from django.urls import path
from . import views

urlpatterns = [
    path('', views.allp, name='all'),
    path('aboutUs', views.aboutUs, name='aboutUs'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('com/<int:id>', views.com, name='com'),
]