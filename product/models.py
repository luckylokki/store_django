from django.db import models


class Category(models.Model):
    slug = models.SlugField(max_length=64)
    name = models.CharField(max_length=64)
    description = models.TextField()


class Product(models.Model):
    slug = models.SlugField(max_length=64)
    name = models.CharField(max_length=64)
    memory = models.CharField(max_length=12)
    discount_available = models.BooleanField(default=False)
    discount = models.CharField(max_length=12)
    available = models.BooleanField(default=False)
    image_url = models.URLField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    quantity = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)