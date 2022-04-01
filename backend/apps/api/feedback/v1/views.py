from rest_framework import generics

from .serializers import FeedbackSerializer


class FeedbackCreateAPIView(generics.CreateAPIView):
    """
    Сохранение отзыва
    """

    serializer_class = FeedbackSerializer
