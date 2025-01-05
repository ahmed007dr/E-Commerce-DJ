from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status


from .serializers import CartDetailSerializers,CartSerializers,OrderDetailSerializers,OrderSerializers,CouponSerializers
from .models import Order,OrderDetail,Cart,CartDetail,Coupon

from products.models import Product
from settings.models import DeliveryFee
from accounts.models import Address

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
    #     return Response({'orders':data})


class OrderDetailsApi(generics.RetrieveAPIView):
    # serializer_class = OrderDetailSerializers # only one item
    # queryset = OrderDetail.objects.all() # only one item 
    serializer_class = OrderSerializers # all data  #related_name='order_details
    queryset = Order.objects.all() # all data 


import datetime

class ApplyCouponApi(generics.GenericAPIView):# video 40 cart API


    def post(self,request,*args,**kwargs):
        user = User.objects.get(username=self.kwargs['username'])  # user from path urls.py
        coupon = get_object_or_404(Coupon,code=request.data['coupon_code'])  # request body # from developer mobile
        delivery_fee = DeliveryFee.objects.last().fee
        cart = Cart.objects.get(user=user, status='in-progress')

        if coupon and coupon.quantity > 0 :
            today_date = datetime.datetime.today().date()  
            if today_date >= coupon.start_date and today_date <= coupon.end_date :
                coupon_value = cart.cart_total * coupon.discount / 100
                sub_total = cart.cart_total - coupon_value
                total = sub_total + delivery_fee

                cart.coupon = coupon
                cart.total_with_coupon = sub_total
                cart.save()

                coupon.quantity -=1
                coupon.save()

                return Response({'message': 'coupon was applied successfully'},status=status.HTTP_202_ACCEPTED)
            else:
                return Response({'message': 'coupon is invalid'},status=status.HTTP_404_NOT_FOUND)
        return Response({'message': 'no coupon was found'},status=status.HTTP_404_NOT_FOUND)
    

class CreateOrderApi(generics.GenericAPIView): # VIDEO 40 CART API
    def post(self,request,*args, **kwargs):
        user = User.objects.get(username=self.kwargs['username'])  # user from path urls.py

        code=request.data['payment_code']  # sent from mobile app # POST > VIEW ||||| data > API
        address = request.data['address_id'] # sent from mobile app # POST > VIEW ||||| data > API

        cart = Cart.objects.get(user=user, status='in-progress')
        cart_details = CartDetail.objects.filter(cart=cart)
        user_address = Address.objects.get(id=address)
        
        # cart > order | cart_detail > order_detail
        new_order = Order.objects.create(
            user = user,
            status = 'received',
            code = code,
            delivery_address = user_address,
            coupon = cart.coupon,
            total_with_coupon = cart.total_with_coupon,
            total = cart.cart_total
        )

        # cart detail 
        for item in cart_details:
            product = Product.objects.get(id=item.products.id)
            OrderDetail.objects.create(
                order = new_order,
                products = product,
                quantity = product.quantity,
                price = product.price,
                total = round(item.quantity * product.price,2)
            )

            # decrease product quantity
            product.quantity -= item.quantity
            product.save()

        # close cart 
        cart.status = 'completed'
        cart.save()

        # sent email here after finish 
        return Response({'message': 'order was created successfully'},status=status.HTTP_201_CREATED)
            
class CartCreateUpdateDelete(generics.GenericAPIView): # method post , get , delete
    def get(self,request,*args, **kwargs):
        user = User.objects.get(username=self.kwargs['username'])  # user from path urls.py
        cart , created = Cart.objects.get_or_create(user=user,status='in-progress')
        data = CartSerializers(cart).data# that's mean return with cart detail not cart (look at serlizers.py ) # POST > VIEW ||||| data > API
        return Response ({'cart':data})
    

    def post(self,request,*args, **kwargs):
        #add or update
        user = User.objects.get(username=self.kwargs['username'])  # user from path urls.py
        product = Product.objects.get(id=request.data['product_id'])
        quantity = int(request.data['quantity']) # POST > VIEW ||||| data > API

        cart = Cart.objects.get(user=user, status="in-progress")

        cart_detail, created = CartDetail.objects.get_or_create(cart=cart, products=product)

        cart_detail.quantity = quantity
        cart_detail.total = round(product.price * cart_detail.quantity, 2)

        cart_detail.save()
        return Response({'message':'cart was updated'},status=status.HTTP_201_CREATED)
            
    def delete(self,request,*args, **kwargs):
        user = User.objects.get(username=self.kwargs['username'])  # user from path urls.py
        cart = Cart.objects.get (user=user,status='in-progress')
        product = CartDetail.objects.get(id=request.data['item-id']) # delete from order details 
        product.delete()
        return Response({'message':'was deleted '},status=status.HTTP_202_ACCEPTED)
 