from apps.api.auth.models import User
from .serializers import UserSerializer
from rest_framework.generics import ListAPIView


class UserAPIList(ListAPIView):
    """
    Список пользователей
    """

    serializer_class = UserSerializer
    queryset = User.objects.filter(dont_show_the_user=False)

