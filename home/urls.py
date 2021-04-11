from django.urls import path
from . import views

urlpatterns = [
    path("", views.project_index, name="home_index"),
    path("<int:pk>/", views.project_detail, name="home_detail"),
]