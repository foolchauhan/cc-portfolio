from django.urls import path
from . import views

urlpatterns = [
    path("", views.resume_index, name="resume_index"),
    path("sample/", views.resume_detail, name="resume_detail"),
]