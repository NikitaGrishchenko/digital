from django.urls import path

from .views import ArticleAPIDetails, ArticleAPIList

app_name = "article"

urlpatterns = [
    path("list/", ArticleAPIList.as_view()),
    path("details/<int:id_article>/", ArticleAPIDetails.as_view()),
]
