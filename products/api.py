from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from rest_framework.permissions import IsAuthenticated

from .models import Product,Brand,Review,ProductImages
from . import serializers



class ProductListAPI(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ['flag', 'name','price']
    search_fields = ['name', 'price']
    permission_classes = [IsAuthenticated] #>>>>>>>>>>>>>>>>>>>>> token API user

class ProductDetailAPI(generics.RetrieveAPIView):  
    queryset = Product.objects.all()
    serializer_class = serializers.ProductDetailsSerializer
    permission_classes = [IsAuthenticated] #>>>>>>>>>>>>>>>>>>>>> token API user


class BrandListAPI(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = serializers.BrandSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ['slug', 'name']
    permission_classes = [IsAuthenticated] #>>>>>>>>>>>>>>>>>>>>> token API user

class BrandDetailAPI(generics.RetrieveAPIView):  
    queryset = Brand.objects.all()
    serializer_class = serializers.BrandDetailsSerializer
    permission_classes = [IsAuthenticated] #>>>>>>>>>>>>>>>>>>>>> token API user
