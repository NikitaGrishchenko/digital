from apps.api.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils.translation import gettext_lazy as _


class Tag(models.Model):
    """
    Тэги публикаций
    """

    name = models.CharField(_("Наименование"), unique=True, max_length=30,)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Тэг публикации")
        verbose_name_plural = _("Тэги публикаций")


class Article(models.Model):
    """
    Модель публикации
    """

    name = models.CharField(_("Наименование"), max_length=255)
    preview = RichTextUploadingField(_("Превью"))
    img = models.ImageField(
        blank=True, null=True, verbose_name=_("Фотография")
    )
    text = RichTextUploadingField(_("Текст"))
    tag = models.ForeignKey(
        Tag,
        on_delete=models.CASCADE,
        verbose_name=_("Тэг"),
        null=True,
        blank=True,
    )
    author = models.ManyToManyField(User, _("Автор"))
    date_of_publication = models.DateTimeField(_("Дата публикации"))
    number_of_views = models.IntegerField(
        _("Количество просмотров публикации"), default=0
    )
    dont_show_the_article = models.BooleanField(
        _("Не показывать публикацию?"),
        help_text="Есть флаг установлен, публикация будет скрыта",
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["date_of_publication"]
        verbose_name = _("Публикация")
        verbose_name_plural = _("Публикации")
