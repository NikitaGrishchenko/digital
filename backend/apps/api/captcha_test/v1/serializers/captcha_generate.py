from apps.api.captcha_test.models import Captcha
from rest_framework import serializers


class CaptchaGenerateSerializer(serializers.ModelSerializer):
    """
    Серилизатор генерации каптчи
    """

    class Meta:
        model = Captcha
        fields = [
            "uuid",
            "image",
        ]
