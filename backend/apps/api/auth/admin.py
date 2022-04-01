from apps.core.utils.admin import BaseAdminMixin
from django.contrib import admin
from django.contrib.admin import ModelAdmin, TabularInline
from django.contrib.auth.admin import GroupAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group as BaseGroup
from django.utils.translation import gettext_lazy as _
from import_export.admin import ImportExportModelAdmin

from .models import Position, ProxyGroup, Social, User


class PositionAdmin(ModelAdmin):
    list_display = ("name",)


class SocialInline(TabularInline):
    model = Social


class SocialAdmin(ModelAdmin):
    list_display = ("name", "link")


@admin.register(User)
class UserAdmin(ImportExportModelAdmin, BaseUserAdmin, BaseAdminMixin):
    list_filter = ("is_superuser",)
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "is_staff",
        "dont_show_the_user",
    )
    list_editable = ("dont_show_the_user",)
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            ("Основная информация"),
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "img",
                    "order",
                    "dont_show_the_user",
                    "position",
                )
            },
        ),
        (("Остальная информация"), {"fields": ("patronymic", "email",)},),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    inlines = [
        SocialInline,
    ]
    list_readonly_not_superuser_fields = (
        "is_superuser",
        "is_staff",
        "last_login",
        "date_joined",
    )


admin.site.unregister(BaseGroup)
admin.site.register(ProxyGroup, GroupAdmin)

admin.site.register(Position, PositionAdmin)
admin.site.register(Social, SocialAdmin)
