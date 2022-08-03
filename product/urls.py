"""User App URL Configuration"""

from django.urls import path
from product.views import product_page, homepage

urlpatterns = [
    path("", homepage),
    path("product/<slug:product>", product_page)
]