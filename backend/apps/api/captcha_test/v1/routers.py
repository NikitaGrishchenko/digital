from django.urls import path

from .views import (
    CaptchaUpdateAPIView,
    EncodeCaptchaAPIView,
    GenerateCaptchaAPIView,
)

app_name = "captcha_test"

urlpatterns = [
    path("generate/", GenerateCaptchaAPIView.as_view()),
    path("update/<slug:uuid>/", CaptchaUpdateAPIView.as_view()),
    path("encode/", EncodeCaptchaAPIView.as_view()),
]
