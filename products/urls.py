from django.urls import path
from .views import ProductList, ProductDetail, BrandList, BrandDetail ,add_review
from . import api


urlpatterns = [
    path('brands/', BrandList.as_view()),  # URL pattern for listing all brands
    path('brands/<slug:slug>/', BrandDetail.as_view()),  # URL pattern for a specific brand
    path('', ProductList.as_view()),  # URL pattern for the product list
    path('<slug:slug>', ProductDetail.as_view()),  # URL pattern for a specific product
    
    path('<slug:slug>/add-review', add_review),  


    #API URLS
    path('api/list',api.ProductListAPI.as_view()),
    path('api/list/<int:pk>',api.ProductDetailAPI.as_view()),
    
    path('api/brands',api.BrandListAPI.as_view()),
    path('api/brands/<int:pk>',api.BrandDetailAPI.as_view()),
    
]
