"""User App URL Configuration"""

from django.urls import path
from product.views import product_page

urlpatterns = [
    path("", product_page)
]