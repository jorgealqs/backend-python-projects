from django.apps import AppConfig  # type: ignore


class LoginConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.login'
    verbose_name = "User Management"
