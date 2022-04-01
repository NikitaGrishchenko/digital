from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CaptchaTestConfig(AppConfig):
    """Default app config"""

    name = "apps.api.captcha_test"
    verbose_name = _("CaptchaTest")

    def ready(self):
        from . import signals  # noqa: F401 # pylint: disable=unused-import
