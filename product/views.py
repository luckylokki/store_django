from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from product.models import Product, Category


class ProductPageDetails(DetailView):
    model = Product
    template_name = 'product.html'


class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'

    def get_context_data(self, **kwargs):
        context = {'product_list': Product.objects.all(), 'category_list': Category.objects.all(),
                   'memory_list': Product.objects.all().values('memory').distinct()}
        return context


class CategoryFilter(ListView):
    model = Product
    template_name = 'product_list.html'

    def get_context_data(self, **kwargs):
        context = {'product_list': Product.objects.filter(category=self.kwargs['category']),
                   'category_list': Category.objects.all(),
                   'memory_list': Product.objects.all().values('memory').distinct()}
        return context


class MemoryFilter(ListView):
    model = Product
    template_name = 'product_list.html'

    def get_context_data(self, **kwargs):
        context = {'product_list': Product.objects.filter(memory=self.kwargs['memory']),
                   'category_list': Category.objects.all(),
                   'memory_list': Product.objects.all().values('memory').distinct()}
        return context

class AddProduct(LoginRequiredMixin, CreateView):

    http_method_names = 'get', 'post'
    model = Product
    fields = '__all__'
    template_name = 'form_product.html'

    def form_valid(self, form):
        form.instance.reporter = self.request.user
        return super().form_valid(form)

class UpdateProduct(LoginRequiredMixin, UpdateView):

    http_method_names = 'get', 'post'
    model = Product
    fields = '__all__'
    template_name = 'form_product.html'

    def form_valid(self, form):
        form.instance.reporter = self.request.user
        return super().form_valid(form)

class DeleteProduct(LoginRequiredMixin, DeleteView):
    
    http_method_names = 'get', 'post'
    model = Product
    template_name = 'delete_confirm.html'
    success_url = reverse_lazy('product_list')

class AddCategory(LoginRequiredMixin, CreateView):

    http_method_names = 'get', 'post'
    model = Category
    fields = '__all__'
    template_name = 'form_category.html'
    success_url = reverse_lazy('product_list')