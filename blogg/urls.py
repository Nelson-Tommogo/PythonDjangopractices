from django.urls import path
from .import views

urlpatterns = [
    path("", views.home, name="blogg-home"),
        path("about/", views.about, name="blogg-about"),
]