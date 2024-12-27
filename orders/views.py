from django.shortcuts import render

# Create your views here.
from .models import Order

def order_list(request):
    data = Order.objects.all()

    return data