from django.urls import path
from . import views

urlpatterns = [
    path('', views.start),
    path('main/', views.main),
    path('guide/', views.guide),
    path('use/', views.use),
    path('setting/', views.setting),
]