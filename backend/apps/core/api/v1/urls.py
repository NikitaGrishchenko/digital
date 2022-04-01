from django.urls import include, path

app_name = "v1"

urlpatterns = [
    path("auth/", include("apps.api.auth.v1")),
    path("article/", include("apps.api.article.v1")),
    path("project/", include("apps.api.project.v1")),
    path("feedback/", include("apps.api.feedback.v1")),
    path("captcha/", include("apps.api.captcha_test.v1")),
]
