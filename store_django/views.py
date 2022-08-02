from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from product.views import product_catalog


def homepage(request: HttpRequest) -> HttpResponse:
    catalog = []
    for item in product_catalog:
        catalog.append({'product': item['product'], 'slug': item['slug']})

    return render(request, 'index.html', {'catalog': catalog})
