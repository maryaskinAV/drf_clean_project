from rest_framework import generics, status
from rest_framework.response import Response

from rest_framework_simplejwt.views import TokenObtainPairView

from users.serializers import UserObtainTokenSerilaizer


class UserObtainTokenView(TokenObtainPairView):
    """
    Get user token for working. Only working on DEBUG!!!!

    :return
    """

    serializer_class = UserObtainTokenSerilaizer


class LoginView(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        """
        fbsdjkfbnksdjbfs dfsd fjklsjdn fl jsbndkfjn

        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return Response(status=status.HTTP_200_OK)


class RegistrationView(generics.CreateAPIView):
    pass


class LogoutView(generics.GenericAPIView):
    pass
