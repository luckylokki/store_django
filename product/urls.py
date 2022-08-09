"""User App URL Configuration"""

from django.urls import path
from product.views import product_page_details, product_list_view

urlpatterns = [
    path("", product_list_view),
    path("product/<slug:slug>/", product_page_details, name="product_details")
]