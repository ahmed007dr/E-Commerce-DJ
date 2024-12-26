from rest_framework import serializers 

from .models import Product, Brand, Review , ProductImages

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta :
        model= ProductImages
        fields = ['image']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    brand = serializers.StringRelatedField()

    # review_count = serializers.SerializerMethodField() # add new column in API view url <<<<<<<<
    # average_rate = serializers.SerializerMethodField()  # Corrected method name

    class Meta:
        model = Product
        # fields = "__all__"
        fields = ['name','brand','get_review_count','get_average_rate','price','subtitle','price','image']

    # def get_review_count(self, object): #get_{field_name}
    #     reviews = object.get_review_count() # review_product دا اسم العلاقه اللي في جدول التقيمات
    #     return reviews

    # def get_average_rate(self,object):
    #     avg = object.get_average_rate()
    #     return avg
    # use it from >>>>>>>@property


class ProductDetailsSerializer(serializers.ModelSerializer):
    brand = serializers.StringRelatedField()
    images = ProductImageSerializer(source='product_images',many=True) # joine new column from anther classs ' product_images' > related
    reviews = ReviewSerializer(source='review_product',many=True) # new column in API view ' with new related 

    
    class Meta:
        model = Product
        fields = "__all__"


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"

class BrandDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"