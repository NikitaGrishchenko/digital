import random

from captcha.image import ImageCaptcha
from django import forms
from django.core.files.base import ContentFile
from service_objects.services import Service

from ..models import Captcha


class CaptchaGenerateService(Service):
    """Сервис генерации каптчи"""

    length = forms.IntegerField()
    answer = forms.CharField(required=False)
    image = forms.ImageField(required=False)
    uuid = forms.UUIDField(required=False)
    width = forms.IntegerField()
    height = forms.IntegerField()

    def process(self):
        length = self.cleaned_data["length"]
        width = self.cleaned_data["width"]
        height = self.cleaned_data["height"]
        answer = self.cleaned_data["answer"]
        image = self.cleaned_data["image"]
        uuid = self.cleaned_data["uuid"]

        answer = self.generate_answer(length)
        image = self.generate_captcha(answer, width, height)

        if uuid:

            captcha = Captcha.objects.get(uuid=uuid)
            setattr(captcha, "image", image)
            setattr(captcha, "answer", answer)
            captcha.save()
            return captcha
        return Captcha.objects.create(answer=answer, image=image)

    def generate_answer(self, length):
        return "".join(
            [
                random.choice("abcdefghijklmnopqrstuvwxyz0123456789")
                for i in range(length)
            ]
        )

    def generate_captcha(self, answer, width, height):
        captcha = ImageCaptcha(width, height)
        return ContentFile(
            captcha.generate(answer).read(),
            f"captcha-{self.generate_answer(10)}.png",
        )
