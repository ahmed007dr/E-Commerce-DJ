from django.shortcuts import render
from django.views.generic import ListView,DetailView
# Create your views here.
from .models import Product , Brand , Review

class ProductList(ListView):
    model = Product


class ProductDetail(DetailView):
    model = Product