from django.urls import path
from DriverManagement import views

urlpatterns = [
    path("", views.home, name="home"),
]