from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu),
    path('test/', views.menu2),
]