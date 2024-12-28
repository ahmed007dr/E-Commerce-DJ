from django.shortcuts import render , redirect

# Create your views here.
from .models import Order , OrderDetail,Cart,CartDetail,Coupon
from products.models import Product
from django.core.paginator import Paginator
from settings.models import DeliveryFee


def order_list(request):
    orders = Order.objects.filter(user=request.user).order_by('-order_time')  
    
    paginator = Paginator(orders, 10)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'orders/order_list.html', {'page_obj': page_obj , 'orders':orders})

def checkout(request):
    cart = Cart.objects.get(user=request.user, status='in-progress')
    cart_detail = CartDetail.objects.filter(cart=cart)
    delivery_fee = DeliveryFee.objects.last().fee
    
    sub_total = cart.cart_total
    discount = 0 
    total = sub_total + delivery_fee

    return render(request,'orders/checkout.html',{
        'cart_detail':cart_detail,
        'delivery_fee':delivery_fee,
        'sub_total':sub_total,
        'total':total,
        "discount":discount,
    })

def add_to_cart(request):
    # Get the product based on the POST data (assuming product_id is passed)
    product = Product.objects.get(id=request.POST['product_id'])
    quantity = int(request.POST['quantity'])

    # Get the cart for the current user with status 'in-progress'
    cart = Cart.objects.get(user=request.user, status="in-progress")
    
    # Use 'products' instead of 'product' (because the field is 'products' according to the error)
    cart_detail, created = CartDetail.objects.get_or_create(cart=cart, products=product)

    # If you want to update the quantity, set it directly (overwriting previous quantity)
    cart_detail.quantity = quantity
    cart_detail.total = round(product.price * cart_detail.quantity, 2)
    
    # Save the updated cart detail
    cart_detail.save()
    
    # Redirect to the product detail page (use the correct slug for redirection)
    return redirect(f'/products/{product.slug}')
