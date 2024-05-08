from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from ms_identity_web.django.msal_views_and_urls import MsalViews

from RestLibrary.urls import router as api_router

msal_urls = MsalViews(settings.MS_IDENTITY_WEB).url_patterns()

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/", include("accounts.urls")),
    path("", include("library.urls"), name="index"),
    path("api/", include(api_router.urls)),
    path(f'{settings.AAD_CONFIG.django.auth_endpoints.prefix}/', include(msal_urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
