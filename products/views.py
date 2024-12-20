from typing import Any
from django.shortcuts import render
from django.views.generic import ListView,DetailView
# Create your views here.
from .models import Product , Brand , Review

class ProductList(ListView):
    model = Product


class ProductDetail(DetailView): # context() - Quryset : product.object.all() : 1:optaion 2:method : orverride
    model = Product
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs) # dict : object product
        context ['reviews'] = Review.objects.filter(product=self.get_object())
        return context