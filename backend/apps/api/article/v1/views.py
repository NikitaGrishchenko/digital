from apps.api.article.models import Article
from apps.api.article.v1.serializers import ArticleSerializer
from django.http import Http404
from django_filters import rest_framework as filters
from rest_framework.generics import ListAPIView, RetrieveAPIView


class ArticleFilter(filters.FilterSet):
    tag = filters.CharFilter(field_name="tag", lookup_expr="name")
    author = filters.CharFilter(field_name="author", lookup_expr="username")

    class Meta:
        model = Article
        fields = [
            "tag",
            "author",
        ]


class ArticleAPIList(ListAPIView):
    """
    Список публикаций
    """

    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = ArticleFilter


class ArticleAPIDetails(RetrieveAPIView):
    """
    Детальный обзор публикаций
    """

    serializer_class = ArticleSerializer
    lookup_url_kwarg = "id_article"

    def get_queryset(self):
        id_article = self.kwargs.get(self.lookup_url_kwarg)
        try:
            return Article.objects.filter(id=id_article)
        except Article.DoesNotExist:
            raise Http404

