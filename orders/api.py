from rest_framework import generics
from django.contrib.auth.models import User

from .serializers import CartDetailSerializers,CartSerializers,OrderDetailSerializers,OrderSerializers,CouponSerializers
from .models import Order,OrderDetail,Cart,CartDetail,Coupon

from products.models import Product
from settings.models import DeliveryFee


class OrderListApi(generics.ListAPIView):
    serializer_class = OrderSerializers
    queryset = Order.objects.all()
