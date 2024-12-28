from django.shortcuts import render

# Create your views here.
from .models import Order , OrderDetail,Cart,CartDetail,Coupon

from django.core.paginator import Paginator

def order_list(request):
    orders = Order.objects.filter(user=request.user)

    paginator = Paginator(orders, 10)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'orders/order_list.html', {'page_obj': page_obj , 'orders':orders})

def checkout(request):
    pass
    return render(request,'orders/checkout.html',{})
