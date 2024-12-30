from django.shortcuts import render , redirect
from django.shortcuts import get_object_or_404 # try exept no error 
# Create your views here.
from .models import Order , OrderDetail,Cart,CartDetail,Coupon
from products.models import Product
from django.core.paginator import Paginator
from settings.models import DeliveryFee
import datetime

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
    

    if request.method =='POST':
        code = request.POST['coupon']
        coupon = get_object_or_404(Coupon,code=code) 

        if coupon and coupon.quantity > 0 : # video 39
            today_date = datetime.datetime.today().date()
            if today_date >= coupon.start_date and today_date <= coupon.end_date:
                coupon_value = round(cart.cart_total / 100 * coupon.discount,2)
                sub_total = cart.cart_total - coupon_value
                total = sub_total + delivery_fee

                cart.coupon = coupon
                cart.total_with_coupon = sub_total
                cart.save()


                return render(request,'orders/checkout.html',{
                    'cart_detail':cart_detail,
                    'delivery_fee':delivery_fee,
                    'sub_total':sub_total,
                    'total':total,
                    "discount":coupon_value # إرسال قيمة الخصم
                })


    # إذا لم يكن هناك كوبون
    # Access the property without parentheses
    sub_total = cart.cart_total
    discount = 0
    total = sub_total + delivery_fee

    return render(request, 'orders/checkout.html', {
        'cart_detail': cart_detail,
        'delivery_fee': delivery_fee,
        'sub_total':sub_total,
        'discount': discount,  # إرسال 0 في حالة عدم وجود خصم
        'total': total,
    })



def add_to_cart(request):
    # Get the product based on the POST data (assuming product_id is passed)
    product = Product.objects.get(id=request.POST['product_id'])
    quantity = int(request.POST['quantity'])

    # Get the cart for the current user with status 'in-progress'
    cart = Cart.objects.get(user=request.user, status="in-progress")
    # print(request.POST)

    # Use 'products' instead of 'product' (because the field is 'products' according to the error)
    cart_detail, created = CartDetail.objects.get_or_create(cart=cart, products=product)

    # If you want to update the quantity, set it directly (overwriting previous quantity)
    cart_detail.quantity = quantity
    cart_detail.total = round(product.price * cart_detail.quantity, 2)
    
    # Save the updated cart detail
    cart_detail.save()
    
    # Redirect to the product detail page (use the correct slug for redirection)
    return redirect(f'/products/{product.slug}')
