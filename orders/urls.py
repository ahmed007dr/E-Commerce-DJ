
from django.urls import path
from .views import checkout, order_list,add_to_cart


urlpatterns = [
    path('',order_list),
    path('checkout/',checkout),
    path('add-to-cart',add_to_cart),

]
