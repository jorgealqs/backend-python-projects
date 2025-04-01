from django.urls import path  # type: ignore
from rest_framework_simplejwt.views import (  # type: ignore
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from .login_views import HomeView

app_name = 'login'

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    # Own Routes
    path('home/', HomeView.as_view(), name='home'),
]
