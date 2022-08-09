from django.contrib import admin
from .models import Category, Product


class ProductModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name", "memory")}


admin.site.register(Category)
admin.site.register(Product, ProductModelAdmin)
