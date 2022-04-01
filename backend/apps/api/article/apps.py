from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ArticleConfig(AppConfig):
    """Default app config"""

    name = "apps.api.article"
    verbose_name = _("Статьи")

    def ready(self):
        from . import signals  # noqa: F401 # pylint: disable=unused-import
