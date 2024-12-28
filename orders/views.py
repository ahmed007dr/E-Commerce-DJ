from django.shortcuts import render

# Create your views here.
from .models import Order , OrderDetail,Cart,CartDetail,Coupon

from django.core.paginator import Paginator

def order_list(request):
    orders = Order.objects.filter(user=request.user).order_by('-order_time')  
    
    paginator = Paginator(orders, 10)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    print (orders)
    return render(request, 'orders/order_list.html', {'page_obj': page_obj , 'orders':orders})

def checkout(request):
    pass
    return render(request,'orders/checkout.html',{})
