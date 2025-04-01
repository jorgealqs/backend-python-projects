from .views import *
from django.urls import path

app_name = 'home'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]
