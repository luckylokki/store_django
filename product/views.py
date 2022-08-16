from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import render
from product.models import Product, Category


def product_page_details(request: HttpRequest, slug: str) -> HttpResponse:
    try:
        context = {"product": Product.objects.get(slug=slug)}
        return render(request, "product.html", context)
    except Product.DoesNotExist:
        raise Http404("Product not found")


def product_list_view(request: HttpRequest) -> HttpResponse:
    context = {"product_list": Product.objects.all(), "category_list": Category.objects.all(),
               "memory_list": Product.objects.all().values("memory").distinct()}
    return render(request, "products_list.html", context)


def category_filter(request: HttpRequest, category: int) -> HttpResponse:
    context = {"product_list": Product.objects.filter(category=category), "category_list": Category.objects.all(),
               "memory_list": Product.objects.all().values("memory").distinct()}
    return render(request, "products_list.html", context)


def memory_filter(request: HttpRequest, memory: str) -> HttpResponse:
    context = {"product_list": Product.objects.filter(memory=memory), "category_list": Category.objects.all(),
               "memory_list": Product.objects.all().values("memory").distinct()}
    return render(request, "products_list.html", context)
