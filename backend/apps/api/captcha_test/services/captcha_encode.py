from django import forms
from service_objects.services import Service

from ..models import Captcha


class CaptchaEncodeService(Service):
    """Сервис проверки каптчи"""

    uuid = forms.UUIDField()
    user_answer = forms.CharField()

    def process(self):
        user_answer = self.cleaned_data["user_answer"]
        uuid = self.cleaned_data["uuid"]

        return self.encode_captcha(uuid, user_answer)

    def encode_captcha(self, uuid, user_answer):
        answer = Captcha.objects.get(uuid=uuid).answer

        return bool(user_answer == answer)
