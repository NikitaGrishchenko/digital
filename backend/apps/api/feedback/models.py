from django.db import models
from django.utils.translation import gettext_lazy as _


class Feedback(models.Model):
    """
    Модель для обратной связи пользователей
    """

    name = models.CharField(_("Имя"), max_length=70, null=True, blank=False)
    email = models.EmailField(
        _("Email"), max_length=254, null=True, blank=False
    )
    appeal = models.TextField(_("Обращение"), null=True, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Отзыв")
        verbose_name_plural = _("Отзывы")

