from rest_framework import serializers 

from .models import Product, Brand, Review

class ProductSerializer(serializers.ModelSerializer):
    brand = serializers.StringRelatedField()

    review_count = serializers.SerializerMethodField() # add new column in API view url <<<<<<<<
    average_rate = serializers.SerializerMethodField()  # Corrected method name

    class Meta:
        model = Product
        fields = "__all__"

    def get_review_count(self, object): #get_{field_name}
        reviews = object.review_product.all().count() # review_product دا اسم العلاقه اللي في جدول التقيمات
        return reviews

    def get_average_rate(self,object):
        total = 0 # sum rate : object
        reviews = object.review_product.all()
        if len(reviews) > 0 :
            for item in reviews:
                total += item.rate # rate column in reviews
            avg = total / len (reviews)
        else:
            avg = 0
        # print(f"Average rate for product {object.id}: {avg}")  
        return avg


class ProductDetailsSerializer(serializers.ModelSerializer):
    brand = serializers.StringRelatedField()
    review_count = serializers.SerializerMethodField() # add new column in API view url <<<<<<<<
    average_rate = serializers.SerializerMethodField()  # Corrected method name

    class Meta:
        model = Product
        fields = "__all__"

    def get_review_count(self, object): #get_{field_name}
        reviews = object.review_product.all().count() # review_product دا اسم العلاقه اللي في جدول التقيمات
        return reviews

    def get_average_rate(self,object):
        total = 0 # sum rate : object
        reviews = object.review_product.all()
        if len(reviews) > 0 :
            for item in reviews:
                total += item.rate # rate column in reviews
            avg = total / len (reviews)
        else:
            avg = 0
        # print(f"Average rate for product {object.id}: {avg}")  
        return avg

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"

class BrandDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"