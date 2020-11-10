from django.urls import path
from . import views

urlpatterns = [
    path('', views.waitboard, name="waitboard"),
    path('enrollboard/', views.enrollboard, name="enrollboard"),
    path("enroll/", views.enroll, name="enroll"),
]
