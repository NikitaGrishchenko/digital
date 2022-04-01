from rest_framework import serializers

from ..models import Feedback


class FeedbackSerializer(serializers.ModelSerializer):
    """Сериализатор вопросов пользователей"""

    class Meta:
        model = Feedback
        fields = "__all__"
