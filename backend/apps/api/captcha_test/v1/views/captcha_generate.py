from apps.api.captcha_test.models import Captcha
from apps.api.captcha_test.services import CaptchaGenerateService
from rest_framework import generics, response

from ..serializers import CaptchaGenerateSerializer


class GenerateCaptchaAPIView(generics.RetrieveAPIView):
    queryset = Captcha.objects.all()
    serializer_class = CaptchaGenerateSerializer

    def get_object(self):
        obj = CaptchaGenerateService.execute(
            {"width": 280, "height": 90, "length": 5}
        )
        self.check_object_permissions(self.request, obj)
        return obj

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return response.Response(serializer.data)
