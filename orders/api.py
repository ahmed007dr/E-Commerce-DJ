from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.response import responses
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