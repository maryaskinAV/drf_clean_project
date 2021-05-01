from django.conf import settings
from django.contrib import admin
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from django.urls import path, re_path, include
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny

API_TITLE = "My custom project"
API_DESCRIPTION = ""
API_DEFAULT_VERSION = ""

schema_view = get_schema_view(
    info=openapi.Info(
        title=API_TITLE,
        description=API_DESCRIPTION,
        default_version=API_DEFAULT_VERSION,
        license=openapi.License(name="BSD Licence"),
    ),
    public=True,
    authentication_classes=(BasicAuthentication,),
    permission_classes=(IsAuthenticatedOrReadOnly, AllowAny),
)

urlpatterns = [
    # base urls
    path("admin/", admin.site.urls),
    # documentation urls
    re_path(r"^docs/(?P<format>\.json|\.yaml)$", schema_view.without_ui(cache_timeout=0), name="schema-json"),
    path("docs/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    # custom urls
    path("auth/", include("users.urls.auth_urls")),
    path("users/", include("users.urls.user_urls")),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()
