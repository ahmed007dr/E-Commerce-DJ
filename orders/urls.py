
from django.urls import path
from .views import checkout, order_list,add_to_cart

from .api import OrderListApi,OrderDetailsApi,ApplyCouponApi

urlpatterns = [
    path('',order_list),
    path('checkout/',checkout),
    path('add-to-cart',add_to_cart),

    #API
    path('api/<str:username>/orders',OrderListApi.as_view()),
    path('api/<str:username>/orders/<int:pk>',OrderDetailsApi.as_view()),
    path('api/<str:username>/applied-coupon/',ApplyCouponApi.as_view()),

]
