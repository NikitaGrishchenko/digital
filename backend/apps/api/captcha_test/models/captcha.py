import uuid

from django.db import models


class Captcha(models.Model):
    """
    Модель для captcha
    """

    uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )

    answer = models.CharField(max_length=50)

    image = models.ImageField(upload_to="captcha/")
