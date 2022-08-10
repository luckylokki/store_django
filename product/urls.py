"""User App URL Configuration"""

from django.urls import path
from product.views import product_page_details, product_list_view, category_filter, memory_filter

urlpatterns = [
    path("", product_list_view, name="product_list"),
    path("product/<slug:slug>/", product_page_details, name="product_details"),
    path("category/<int:category>/", category_filter, name="category_filter"),
    path("filter/<str:memory>/", memory_filter, name="memory_filter")
]