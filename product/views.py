from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

product_catalog = [
    {
        "id": 1,
        "product": "Iphone 11",
        "slug": "iphone-11-128",
        "memory": "128gb",
        "available": True,
        "image": "https://www.tradeinn.com/f/13735/137354156/apple-iphone-11-128gb-6.1.jpg",
        "description": "Description for apple product",
        "price": 22_000.00,
    },
    {
        "id": 2,
        "product": "Iphone 12",
        "slug": "iphone-12-128",
        "memory": "128gb",
        "available": False,
        "image": "https://www.tradeinn.com/f/13782/137821875/apple-iphone-12-4gb-128gb-6.1.jpg",
        "description": "Description for apple product",
        "price": 43_000.00
    },
    {
        "id": 3,
        "product": "MacBook Pro M1",
        "slug": "macbook-pro-m1-256",
        "memory": "256gb",
        "available": True,
        "image": "https://www.tradeinn.com/f/13841/138412956/apple-macbook-pro-14-m1-pro-16gb--512gb-ssd-Ноутбук.jpg",
        "description": "Description for apple product",
        "price": 89_000.00
    },
]


def product_page(request: HttpRequest, product: str) -> HttpResponse:
    for item in product_catalog:
        if item['slug'] == product:
            context = item
    return render(request, 'product.html', context)


def homepage(request: HttpRequest) -> HttpResponse:
    context = []
    for item in product_catalog:
        context.append({'product': item['product'], 'slug': item['slug'], 'image': item['image'], 'memory': item['memory'], 'available': item['available']})
    return render(request, 'products_list.html', {'catalog': context})