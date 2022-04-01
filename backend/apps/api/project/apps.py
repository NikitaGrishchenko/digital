from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ProjectConfig(AppConfig):
    """Default app config"""

    name = "apps.api.project"
    verbose_name = _("Проекты")

    def ready(self):
        from . import signals  # noqa: F401 # pylint: disable=unused-import
