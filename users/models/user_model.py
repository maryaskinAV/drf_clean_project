from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.base_user import BaseUserManager

from utils.utils import upload_instance_image


class UserManager(BaseUserManager):
    """ Менеджер для перекрытой модели пользователя """

    use_in_migrations = True

    def _create_user(self, email, password, **extra_kwargs):
        if password is not None:
            try:
                validate_password(password)
            except ValidationError as e:
                raise ValueError({"password": str(e.message)})
        else:
            raise ValueError({"password": _("Password can't be set. Update password and try again.")})

        if extra_kwargs.get("email"):
            email = self.normalize_email(extra_kwargs.pop("email"))

    def create_user(self, email, password=None, **extra_kwargs):
        """ Create simple user """
        return self._create_user(email, password, **extra_kwargs)

    def create_superuser(self, email, password=None, **extra_kwargs):
        """ Create superuser account """
        extra_kwargs.setdefault("is_", True)
        extra_kwargs.setdefault("is_", True)
        extra_kwargs.setdefault("is_", True)
        return self._create_user(email, password, **extra_kwargs)


class User(AbstractUser):
    """
    Переопределенная модель пользователя
    """

    username = None
    email = models.EmailField(_("User email:"), unique=True, max_length=125)
    first_name = models.CharField(_("First name"), max_length=100)
    last_name = models.CharField(_("Last name"), max_length=100)
    avatar = models.ImageField(_("User image avatar"), upload_to=upload_instance_image, blank=True, null=True)

    objects = UserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ("first_name", "last_name")

    def __str__(self):
        return self.email

    class Meta:
        ordering = ("-id",)
        verbose_name = _("User")
        verbose_name_plural = _("Users")
