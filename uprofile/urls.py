"""User App URL Configuration"""

from django.urls import path
from uprofile.views import user_profile, signin_view, signout_view,signup_view, deactivate_user_view, user_profile_edit, change_profile_password

urlpatterns = [
    path('profile/', user_profile, name='user_profile'),
    path('signin/', signin_view, name='signin'),
    path('signout/', signout_view, name='signout'),
    path('signup/', signup_view, name='signup'),
    path('profile/deactivate/', deactivate_user_view, name='deactivate'),
    path('profile/edit/', user_profile_edit, name='edit_profile'),
    path('profile/change_password/', change_profile_password, name='change_password')
]
