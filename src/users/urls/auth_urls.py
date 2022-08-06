from django.urls import path, re_path

from users.views import UserObtainTokenView, LoginView, RegistrationView, LogoutView

urlpatterns = [
    path("obtain_token/", UserObtainTokenView.as_view(), name="obtain-user-token"),
    path("login/", LoginView.as_view(), name="base-login"),
    path("registration/", RegistrationView.as_view(), name="base-registration"),
    path("logout/", LogoutView.as_view(), name="logout-user"),
]
