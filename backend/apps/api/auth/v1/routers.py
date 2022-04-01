from django.urls import path

from .views import UserAPIList

app_name = "auth"

urlpatterns = [
    path("list/", UserAPIList.as_view()),
]
