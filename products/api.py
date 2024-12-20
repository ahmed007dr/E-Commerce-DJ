from rest_framework import generics
from .models import Product,Brand,Review,ProductImages
from . import serializers



class ProductListAPI(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductDetailsSerializer

class ProductDetailAPI(generics.RetrieveAPIView):  
    queryset = Product.objects.all()
    serializer_class = serializers.ProductDetailsSerializer
