from django.conf.urls import include
from django.urls import path

from .views import UserAPIList

app_name = "auth"

urlpatterns = [
    # path("token/", include("dj_rest_auth.urls")),
    path("list/", UserAPIList.as_view()),
]
