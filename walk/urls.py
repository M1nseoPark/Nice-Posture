from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu),
    path('beginner/', views.beginner),
    path('intermediate/', views.intermediate),
    path('senior/', views.senior),
]