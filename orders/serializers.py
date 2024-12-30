from rest_framework import serializers
from .models import Cart , CartDetail , Order , OrderDetail , Coupon

class CartDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = CartDetail
        fields = '__all__'


class CartSerializers(serializers.ModelSerializer):
    cart_detail = CartDetailSerializers(many=True)
    class Meta:
        model = Cart
        fields = '__all__'

class OrderDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = '__all__'


class OrderSerializers(serializers.ModelSerializer):
    order_detail = OrderDetailSerializers(many=True)
    class Meta:
        model = Order
        fields = '__all__'

class CouponSerializers(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = '__all__'


