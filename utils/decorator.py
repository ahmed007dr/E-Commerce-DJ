
# def decorator(func):
#     def wrapper():
#         print('first')
#         func() #excute
#         print('last')

#     return wrapper


# @decorator
# def x():
#     print('hello')
# x()


from django.shortcuts import redirect
from functools import wraps
import datetime
from orders.models import Cart,Coupon


def fetch_cart(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        try:
            cart = Cart.objects.get(user=request.user, status='in-progress')
            request.cart = cart  # Attach the cart to the request object
        except Cart.DoesNotExist:
            return redirect('cart_empty')  # Redirect to a "Cart Empty" page
        return view_func(request, *args, **kwargs)
    return wrapper

def validate_coupon(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        code = request.POST.get('coupon')
        if code:
            try:
                coupon = Coupon.objects.get(code=code, quantity__gt=0)
                today_date = datetime.datetime.today().date()
                if today_date >= coupon.start_date and today_date <= coupon.end_date:
                    request.coupon = coupon  # Attach the coupon to the request object
                else:
                    request.coupon = None  # Invalid coupon
            except Coupon.DoesNotExist:
                request.coupon = None  # No coupon found
        else:
            request.coupon = None  # No coupon submitted
        return view_func(request, *args, **kwargs)
    return wrapper
