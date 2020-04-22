from django.urls import path
from . import views

urlpatterns = [
    path("", views.resume_index, name="resume_index"),
    path("sample/", views.resume_detail, name="resume_detail"),
    path("sample2/", views.resume_detail2, name="resume_detail2"),
]