from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView,DetailView
# Create your views here.
from .models import Product , Brand , Review ,ProductImages
from django.shortcuts import get_object_or_404

class ProductList(ListView):
    model = Product


class ProductDetail(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # Get the default context with the product object
        context['reviews'] = Review.objects.filter(product=self.get_object())  # Add reviews to context
        context['images'] = ProductImages.objects.filter(product=self.get_object())  # Fix typo here
        context['related'] = Product.objects.filter(brand=self.get_object().brand)[:10]
        return context
    

class BrandList(ListView):
    model = Brand


class BrandDetail(ListView):
    model = Product
    template_name = 'products/brand_detail.html'

    def get_queryset(self):
        # Ensure we're fetching the correct brand based on the slug
        brand = get_object_or_404(Brand, slug=self.kwargs['slug'])
        # Return products that belong to this brand
        return Product.objects.filter(brand=brand)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add the brand to the context so we can display its name and details
        context['brand'] = get_object_or_404(Brand, slug=self.kwargs['slug'])
        return context


# class BrandDetail(DetailView):
#     model = Brand
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)  
#         context['products'] = Product.objects.filter(brand = self.get_object())

#         return context
