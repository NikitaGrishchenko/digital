from apps.api.auth.models import Position, Social, User
from rest_framework import serializers


class PositionSerializer(serializers.ModelSerializer):
    """Сериализатор должности пользователя"""

    class Meta:
        model = Position
        fields = ["name"]


class SocialSerializer(serializers.ModelSerializer):
    """Сериализатор социальных сетей пользователя"""

    class Meta:
        model = Social
        fields = ["id", "icon", "link"]


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор пользователя"""

    social = serializers.SerializerMethodField()
    position = PositionSerializer()

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "img",
            "social",
            "position",
            "order",
            "dont_show_the_user",
        ]

    def get_social(self, instance):
        return [
            SocialSerializer(social).data
            for social in Social.objects.filter(user=instance.pk)
        ]
