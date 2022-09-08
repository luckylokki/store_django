"""User App URL Configuration"""

from django.urls import path
from product.views import ProductPageDetails, ProductListView, CategoryFilter, MemoryFilter

urlpatterns = [
    path("", ProductListView.as_view(), name="product_list"),
    path("product/<slug:slug>/", ProductPageDetails.as_view(), name="product_details"),
    path("category/<int:category>/", CategoryFilter.as_view(), name="category_filter"),
    path("filter/<str:memory>/", MemoryFilter.as_view(), name="memory_filter")
]