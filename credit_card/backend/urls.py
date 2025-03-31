from django.contrib import admin  # type: ignore
from django.urls import path  # type: ignore

urlpatterns = [
    path("admin/", admin.site.urls),
]
