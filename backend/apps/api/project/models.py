from django.db import models
from django.utils.translation import gettext_lazy as _


class Project(models.Model):
    """
    Модель списка проектов
    """

    name = models.CharField(_("Наименование"), max_length=255)
    description = models.CharField(
        _("Описание"), max_length=255, null=True, blank=True
    )
    link = models.URLField(_("Ссылка"), max_length=200)
    img = models.ImageField(
        blank=True, null=True, verbose_name=_("Фотография")
    )
    order = models.IntegerField(_("Порядок вывода"), null=True, blank=True)
    dont_show_the_project = models.BooleanField(
        _("Не показывать проект?"),
        help_text="Есть флаг установлен, проект будет скрыт",
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = [
            "order",
        ]
        verbose_name = _("Проект")
        verbose_name_plural = _("Проект")
