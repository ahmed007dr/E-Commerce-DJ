from rest_framework import serializers 

from .models import Product, Brand, Review

class ProductSerializer(serializers.ModelSerializer):
    brand = serializers.StringRelatedField()

    review_count = serializers.SerializerMethodField() # add new column in API view url <<<<<<<<

    class Meta:
        model = Product
        fields = "__all__"

    def get_review_count(self, obj): #get_{field_name}
        reviews = object.review_product.all().count() # review_product دا اسم العلاقه اللي في جدول التقيمات
        return reviews


class ProductDetailsSerializer(serializers.ModelSerializer):
    brand = serializers.StringRelatedField()

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