from django.contrib import admin  # type: ignore
from django.urls import path, include  # type: ignore

urlpatterns = [
    path("admin/", admin.site.urls),
    path("home/", include("apps.home.urls")),
    path("api/v1/", include("apps.login.router")),
]
