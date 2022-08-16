"""User App URL Configuration"""

from django.urls import path
from uprofile.views import user_profile, signin_view, signout_view,signup_view, deactivate_user_view

urlpatterns = [
    path('profile/', user_profile, name='user_profile'),
    path('signin/', signin_view, name='signin'),
    path('signout/', signout_view, name='signout'),
    path('signup/', signup_view, name='signup'),
    path('profile/deactivate/', deactivate_user_view, name='deactivate')
]
