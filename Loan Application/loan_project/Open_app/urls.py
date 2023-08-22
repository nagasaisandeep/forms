from django.urls import path
from .import views

urlpatterns = [
    path('', views.Application, name = 'Application'),
    #path('success/', views.Appli),
]