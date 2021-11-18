from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.urls import reverse_lazy

from .forms import CreateProductForm, UpdateProductForm
from .models import *
from .utils import cartData


class SearchResultsView(ListView):
    queryset = Product.objects.all()
    template_name = 'store/store.html'
    context_object_name = 'products'

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(Q(name__icontains=q) | Q(description__icontains=q))
        return queryset

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        data = cartData(self.request)
        cartItems = data['cartItems']
        context['cartItems'] = cartItems
        return context


class ProductDetailsView(DetailView):
    queryset = Product.objects.all()
    template_name = 'store/product_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = cartData(self.request)
        cartItems = data['cartItems']
        context['cartItems'] = cartItems
        return context


class CreatePostView(LoginRequiredMixin, CreateView):
    queryset = Product.objects.all()
    template_name = 'store/create_product.html'
    form_class = CreateProductForm
    success_url = reverse_lazy('store')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


class IsAuthorMixin(UserPassesTestMixin):
    def test_func(self):
        product = self.get_object()
        return self.request.user.is_authenticated and self.request.user == product.user


class UpdateProductView(IsAuthorMixin, UpdateView):
    queryset = Product.objects.all()
    template_name = 'store/update_product.html'
    form_class = UpdateProductForm

    def get_success_url(self):
        product = self.get_object()
        return product.get_absolute_url()

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        data = cartData(self.request)
        cartItems = data['cartItems']
        context['cartItems'] = cartItems
        return context


class DeleteProductView(IsAuthorMixin, DeleteView):
    queryset = Product.objects.all()
    template_name = 'store/delete_product.html'
    success_url = reverse_lazy('store')

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        data = cartData(self.request)
        cartItems = data['cartItems']
        context['cartItems'] = cartItems
        return context