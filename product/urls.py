'''User App URL Configuration'''

from django.urls import path
from product.views import ProductPageDetails, ProductListView, CategoryFilter, MemoryFilter, AddProduct, UpdateProduct, DeleteProduct, AddCategory

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('product/<slug:slug>/', ProductPageDetails.as_view(), name='product_details'),
    path('category/<int:category>/', CategoryFilter.as_view(), name='category_filter'),
    path('filter/<str:memory>/', MemoryFilter.as_view(), name='memory_filter'),
    path('add/', AddProduct.as_view(), name='add_product'),
    path('update/<slug:slug>/', UpdateProduct.as_view(), name='update_product'),
    path('delete/<slug:slug>', DeleteProduct.as_view(), name='delete_product'),
    path('add-category/', AddCategory.as_view(), name='add_category'),

]