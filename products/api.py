from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .models import Product,Brand,Review,ProductImages
from . import serializers



class ProductListAPI(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductDetailsSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ['flag', 'name','price']
    search_fields = ['name', 'price']

class ProductDetailAPI(generics.RetrieveAPIView):  
    queryset = Product.objects.all()
    serializer_class = serializers.ProductDetailsSerializer


class BrandListAPI(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = serializers.BrandDetailsSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ['slug', 'name']

class BrandDetailAPI(generics.RetrieveAPIView):  
    queryset = Brand.objects.all()
    serializer_class = serializers.BrandDetailsSerializer
