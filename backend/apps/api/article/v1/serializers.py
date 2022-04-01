from apps.api.auth.v1.serializers import UserSerializer
from rest_framework import serializers

from ..models import Article, Tag


class TagSerializer(serializers.ModelSerializer):
    """ Сериализатор тега """

    class Meta:
        model = Tag
        fields = ["name"]


class ArticleSerializer(serializers.ModelSerializer):
    """ Сериализатор публикации """

    author = UserSerializer(many=True)
    tag = TagSerializer()
    date_of_publication = serializers.DateTimeField(format="iso-8601")

    class Meta:
        model = Article
        fields = "__all__"
