from rest_framework import response, status, views

from ..serializers import CaptchaEncodeSerializer


class EncodeCaptchaAPIView(views.APIView):
    serializer_class = CaptchaEncodeSerializer

    def post(self, request, *args, **kwargs):
        return self.encode(request, *args, **kwargs)

    def encode(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.proccess_captcha()

        return response.Response(status=status.HTTP_200_OK)
