from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import Group, PermissionsMixin, UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class ProxyGroup(Group):
    class Meta:
        proxy = True
        verbose_name = _("group")
        verbose_name_plural = _("groups")

class Position(models.Model):
    """
    Должность пользователя
    """

    name = models.CharField(_("Наименование"), max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Должность пользователя")
        verbose_name_plural = _("Должности пользователя")

class User(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_(
            "Required. 150 characters or fewer. Letters, "
            "digits and @/./+/-/_ only."
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
    first_name = models.CharField(_("first name"), max_length=30, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    patronymic = models.CharField(
        _("Отчество"), max_length=150, blank=True, null=True
    )
    position = models.ForeignKey(
        Position,
        on_delete=models.CASCADE,
        verbose_name=_("Должность"),
        null=True,
        blank=True,
    )

    img = models.ImageField(
        blank=True, null=True, verbose_name=_("Фотография")
    )
    order = models.IntegerField(_("Порядок вывода"), null=True, blank=True)
    dont_show_the_user = models.BooleanField(
        _("Не показывать пользователя?"),
        help_text="Есть флаг установлен, пользователь будет скрыт",
        default=False,
    )
    email = models.EmailField(_("email address"), blank=True)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_(
            "Designates whether the user can log into this admin site."
        ),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    class Meta:
        swappable = "AUTH_USER_MODEL"
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

class Social(models.Model):
    """
    Социальные сети пользователя
    """

    user = models.ForeignKey(
        User,
        verbose_name=_("Пользователь"),
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    name = models.CharField(
        _("Наименование"), max_length=50, null=True, blank=True,
    )

    icon = models.CharField(
        _("Иконка"),
        max_length=50,
        help_text="Необходим класс mdi",
        null=True,
        blank=True,
    )

    link = models.URLField(
        _("Ссылка на социальную сеть"), max_length=200, null=True, blank=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Социальная сеть пользователя")
        verbose_name_plural = _("Социальные сети пользователя")
