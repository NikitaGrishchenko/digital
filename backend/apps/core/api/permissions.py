from django.conf import settings
from rest_framework.permissions import BasePermission


class BlockCORS(BasePermission):
    def has_permission(self, request, view) -> bool:
        return (
            settings.DEBUG
            or str(request.META.get("HTTP_REFERER")).find(settings.SITE_DOMAIN)
            > -1
        )
