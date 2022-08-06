from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserObtainTokenSerilaizer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["id"] = user.id
        token["email"] = user.email
        return token
