from django.views.generic import ListView, DetailView

from product.models import Product, Category


class ProductPageDetails(DetailView):
    model = Product
    template_name = 'product.html'


class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'

    def get_context_data(self, **kwargs):
        context = {"product_list": Product.objects.all(), "category_list": Category.objects.all(),
                   "memory_list": Product.objects.all().values("memory").distinct()}
        return context


class CategoryFilter(ListView):
    model = Product
    template_name = 'product_list.html'

    def get_context_data(self, **kwargs):
        context = {"product_list": Product.objects.filter(category=self.kwargs['category']),
                   "category_list": Category.objects.all(),
                   "memory_list": Product.objects.all().values("memory").distinct()}
        return context


class MemoryFilter(ListView):
    model = Product
    template_name = 'product_list.html'

    def get_context_data(self, **kwargs):
        context = {"product_list": Product.objects.filter(memory=self.kwargs['memory']),
                   "category_list": Category.objects.all(),
                   "memory_list": Product.objects.all().values("memory").distinct()}
        return context

