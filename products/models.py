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
    brand = models.ForeignKey("Brand",related_name='product_brand',on_delete=models.SET_NULL,null=True)
    slug = models.SlugField(blank=True,null=True,unique=True)

    def save(self, *args , **kwargs):
        self.slug = slugify(self.name) # slugify ===> convert text to slug "CEO"
        super(Product,self).save(*args , **kwargs) #=======> 

    def __str__(self):
        return self.name
    

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
        return str(self.user)  # هذا سيعرض اسم المستخدم
    
    