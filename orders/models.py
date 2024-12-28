from django.db import models
from django.contrib.auth.models import User
from utils.generate import generate_code
from django.utils import timezone
from products.models import Product
from accounts.models import Address
import datetime

ORDER_STATUS = (
    ('received', 'received'),
    ('processed', 'processed'),
    ('shipped', 'shipped'),
    ('delivered', 'delivered')
)
class Order(models.Model): #INVOICE
    user = models.ForeignKey(User,related_name='order_owner',on_delete=models.SET_NULL,null=True,blank=True)
    status = models.CharField(choices=ORDER_STATUS,max_length=12)
    code = models.CharField(default=generate_code,max_length=8)
    order_time = models.DateTimeField(default=timezone.now)
    delivery_time = models.DateTimeField(null=True,blank=True)
    delivery_address = models.ForeignKey(Address,related_name='delivery_address',on_delete=models.SET_NULL,null=True,blank=True)
    coupon = models.ForeignKey("Coupon",related_name='order_coupon',on_delete=models.SET_NULL,null=True,blank=True)
    total = models.FloatField()
    total_with_coupon = models.FloatField(null=True,blank=True)

    def __str__(self) -> str:
        return f'{self.user} - {self.total} ' 


class OrderDetail(models.Model): #INVOICE
    order = models.ForeignKey(Order,related_name='order_details',on_delete=models.CASCADE)
    products =  models.ForeignKey(Product,related_name = 'orderdetail_product',on_delete=models.SET_NULL,null=True,blank=True)
    quantity = models.IntegerField()
    price = models.FloatField()
    total = models.FloatField(null=True,blank=True)



    def __str__(self) -> str:
        return f'{self.quantity} - {self.total} ' 

CART_STATUS = (
    ('in-progress', 'in-progress'),
    ('completed', 'completed'),
)
class Cart(models.Model):
    user = models.ForeignKey(User,related_name='cart_owner',on_delete=models.SET_NULL,null=True,blank=True)
    status = models.CharField(choices=CART_STATUS,max_length=12)
    coupon = models.ForeignKey("Coupon",related_name='cart_coupon',on_delete=models.SET_NULL,null=True,blank=True)
    total_with_coupon = models.FloatField(null=True,blank=True)

    @property
    def cart_total(self): # video 38 
        total = 0
        for item in self.cart_details.all():
            total += item.total
        return round(total,2)

    def __str__(self) -> str:
        return f'name of client {self.user} - {self.status} - cart total for user {self.cart_total}' 
    

class CartDetail(models.Model):
    cart = models.ForeignKey(Cart,related_name='cart_details',on_delete=models.CASCADE)
    products =  models.ForeignKey(Product,related_name = 'cartdetail_product',on_delete=models.SET_NULL,null=True,blank=True)
    quantity = models.IntegerField(default=1)
    total = models.FloatField(null=True,blank=True)

    def __str__(self) -> str:
        return f'{self.cart} - {self.quantity} - {self.total} ' 


class Coupon(models.Model): # only for admin
    code = models.CharField(max_length=20)
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(null=True,blank=True)
    quantity = models.IntegerField()
    discount = models.FloatField()

    def save(self,*args,**kwargs):
        week = datetime.timedelta(days=7)
        self.end_date = self.start_date + week
        super(Coupon,self).save(*args,**kwargs)
    
    
    def __str__(self) -> str:
        return f'{self.code} - {self.start_date} - {self.end_date} - {self.quantity} - {self.discount} ' 

    