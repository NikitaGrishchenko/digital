from rest_framework import generics, response

from ...services import CaptchaGenerateService
from ..serializers import CaptchaGenerateSerializer


class CaptchaUpdateAPIView(generics.RetrieveAPIView):
    serializer_class = CaptchaGenerateSerializer
    lookup_field = "uuid"

    def get_object(self):
        lookup_url_kwarg = self.lookup_field
        assert lookup_url_kwarg in self.kwargs, "UUID is required"

        obj = CaptchaGenerateService.execute(
            {
                "width": 280,
                "height": 90,
                "length": 5,
                "uuid": self.kwargs[lookup_url_kwarg],
            }
        )
        self.check_object_permissions(self.request, obj)

        return obj

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return response.Response(serializer.data)
