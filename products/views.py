from typing import Any
from django.shortcuts import render
from django.views.generic import ListView,DetailView
# Create your views here.
from .models import Product , Brand , Review ,ProductImages

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


class BrandDetail(DetailView):
    pass