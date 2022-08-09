from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import render
from product.models import Product


def product_page_details(request: HttpRequest, slug: str) -> HttpResponse:
    try:
        context = {"product": Product.objects.get(slug=slug)}
        return render(request, "product.html", context)
    except Product.DoesNotExist:
        raise Http404("Product not found")


def product_list_view(request: HttpRequest) -> HttpResponse:
    context = {"product_list": Product.objects.all()}
    return render(request, "products_list.html", context)