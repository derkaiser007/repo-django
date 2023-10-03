from django.urls import path
from . import views

urlpatterns=[
    path("", views.index, name="index"),
    path("niraj", views.niraj, name="niraj"),
    path("<str:name>", views.greet, name="greet")
]