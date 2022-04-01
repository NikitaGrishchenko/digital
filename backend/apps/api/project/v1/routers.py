from django.urls import path

from .views import ProjectAPIList

app_name = "project"

urlpatterns = [
    path("list/", ProjectAPIList.as_view()),
]
