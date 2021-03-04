from django.urls import path
from . import views

urlpatterns = [
    path("", views.myView),
    path("new/", views.newView),
]
