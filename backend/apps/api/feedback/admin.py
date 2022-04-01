from django.contrib import admin

from .models import Feedback


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    """Админка отзывов"""

    list_display = ("name", "email")

    def has_add_permission(self, request):
        """Запрещает добавление из админки"""
        return False

    def has_change_permission(self, request, obj=None):
        """Запрещает редактирование из админки"""
        return False
