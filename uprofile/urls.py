"""User App URL Configuration"""

from django.urls import path
from uprofile.views import user_profile

urlpatterns = [
    path('profile/', user_profile, name='user_profile'),
]
