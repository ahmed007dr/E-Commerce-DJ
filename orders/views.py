from django.shortcuts import render

# Create your views here.
from .models import Order , OrderDetail,Cart,CartDetail,Coupon

def order_list(request):
    data = Order.objects.filter(user=request.user)

    return render(request,'orders/order_list.html',{'orders':data})


def checkout(request):
    pass
    return render(request,'orders/checkout.html',{})
