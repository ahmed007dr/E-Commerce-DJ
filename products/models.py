from typing import Iterable
from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify # convert text to slug
# Create your models here.


FLAG_TYPS =(
    ('New','New'),
    ('Sale','Sale'),
    ('Feature','Feature'))

class Product(models.Model):
    name = models.CharField(max_length=120)
    flag = models.CharField(max_length=10)
    price = models.FloatField(max_length=5)
    image = models.ImageField(upload_to='product')
    sku = models.IntegerField()
    subtitle = models.TextField(max_length=500)
    description = models.TextField(max_length=10000)
    tags = TaggableManager()
    quantity = models.IntegerField(default=1)
    brand = models.ForeignKey("Brand",related_name='product_brand',on_delete=models.SET_NULL,null=True)
    slug = models.SlugField(blank=True,null=True,unique=True)

    def save(self, *args , **kwargs):
        self.slug = slugify(self.name) # slugify ===> convert text to slug "CEO"
        super(Product,self).save(*args , **kwargs) #=======> 

    def __str__(self):
        return self.name
    
    #take it from serializers.py
    @property # NEW COLUMN IN DB
    def get_review_count(self): #get_{field_name}
        reviews = self.review_product.all().count() # review_product دا اسم العلاقه اللي في جدول التقيمات
        return reviews
    
    @property #new column in DB
    def get_average_rate(self):
        total = 0 # sum rate : object
        reviews = self.review_product.all()
        if len(reviews) > 0 :
            for item in reviews:
                total += item.rate # rate column in reviews
            avg = total / len (reviews)
        else:
            avg = 0
        return avg


class ProductImages(models.Model):
    product = models.ForeignKey(Product, related_name='product_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/')

class Brand(models.Model):
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to='brand')
    slug = models.SlugField(unique=True, blank=True, null=True)  


    def save(self, *args , **kwargs):
        self.slug = slugify(self.name) # slugify ===> convert text to slug "CEO"
        super(Brand,self).save(*args , **kwargs) #=======> 


    def __str__(self):
        return self.name
    
    
class Review(models.Model):
    user = models.ForeignKey(User, related_name='review_user', on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, related_name='review_product', on_delete=models.CASCADE)
    review = models.TextField(max_length=100)
    rate = models.IntegerField(choices={(i, i) for i in range(1, 6)})
    create_at = models.TimeField(default=timezone.now)


    def __str__(self):
        return f'Review by {self.user} on {self.product} - Rating: {self.rate} - {self.create_at}'
    
    