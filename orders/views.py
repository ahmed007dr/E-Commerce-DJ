from django.shortcuts import render

# Create your views here.
from .models import Order , OrderDetail,Cart,CartDetail,Coupon

def order_list(request):
    data = Order.objects.all()

    return data