from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.response import responses
from django.shortcuts import get_object_or_404

from .serializers import CartDetailSerializers,CartSerializers,OrderDetailSerializers,OrderSerializers,CouponSerializers
from .models import Order,OrderDetail,Cart,CartDetail,Coupon

from products.models import Product
from settings.models import DeliveryFee


class OrderListApi(generics.ListAPIView):
    serializer_class = OrderSerializers
    queryset = Order.objects.all()

    def get_queryset(self): # plan A
        queryset = super(OrderListApi,self).get_queryset()
        user = User.objects.get(username =self.kwargs['username']) # user from path urls.py
        queryset = queryset.filter(user=user)
        return queryset


    # def List(self,request,*args,**kwargs): # plan B
    #     queryset = super(OrderListApi,self).get_queryset()
    #     user = User.objects.get(username =self.kwargs['username']) # user from path urls.py
    #     queryset = queryset.filter(user=user)
    #     data = OrderSerializers(queryset,many=True).data
    #     return responses({'orders':data})
class OrderDetailsApi(generics.RetrieveAPIView):
    # serializer_class = OrderDetailSerializers # only one item
    # queryset = OrderDetail.objects.all() # only one item 
    serializer_class = OrderSerializers # all data  #related_name='order_details
    queryset = Order.objects.all() # all data 


import datetime

class ApplyCouponApi(generics.GenericAPIView):

    def post(self,request,*args,**kwargs):
        user = User.objects.get(username=self.kwargs['username'])  # user from path urls.py
        coupon = get_object_or_404(Coupon,code=request.data['coupon_code'])  # request body # from developer mobile
        delivery_fee = DeliveryFee.objects.last().fee
        cart = Cart.objects.get(user=user, status='in-progress')

        if coupon and coupon.quantity > 0 :
            today_date = datetime.datetime.today.date()
            if today_date >= coupon.start_date and today_date <= coupon.end_date :
                coupon_value = cart.cart_total * coupon.discount / 100
                sub_total = cart.cart_total - coupon_value
                total = sub_total + delivery_fee

                cart.coupon = coupon
                cart.total_with_coupon = sub_total
                cart.save()

                coupon.quantity -=1
                coupon.save()

                return responses({'message': 'coupon was applied successfully'})
            else:
                return responses({'message': 'coupon is invalid'})
        return responses({'message': 'no coupon was found'})