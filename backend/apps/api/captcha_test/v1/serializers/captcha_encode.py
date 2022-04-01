from rest_framework import serializers

from ...models import Captcha
from ..utils import captcha_is_valid


class CaptchaEncodeSerializer(serializers.ModelSerializer):
    """
    Серилизатор разгадывания каптчи
    """

    user_answer = serializers.CharField(write_only=True)
    uuid = serializers.CharField()

    def validate(self, data):
        uuid = data["uuid"]
        user_answer = data["user_answer"]

        if not captcha_is_valid(uuid, user_answer):
            raise serializers.ValidationError("CAPTCHA is not valid")
        return data

    def proccess_captcha(self, **kwargs):
        validated_data = {**self.validated_data, **kwargs}

        uuid = validated_data["uuid"]

        instance = Captcha.objects.get(uuid=uuid).delete()

        return instance

    class Meta:
        model = Captcha
        fields = [
            "uuid",
            "user_answer",
        ]
