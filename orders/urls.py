
from django.urls import path
from .views import checkout, order_list


urlpatterns = [
    path('',order_list),
    path('checkout/',checkout)

]
