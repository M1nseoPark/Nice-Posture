from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu),
    path('posture/', views.posture),
    path('neck_shoulder/', views.neck_shoulder),
    path('waist/', views.waist),
    path('knee/', views.knee),
    path('back/', views.back),
    path('body/', views.body),
]