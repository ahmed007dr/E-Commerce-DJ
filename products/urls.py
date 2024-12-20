from django.urls import path
from .views import ProductList, ProductDetail, BrandList, BrandDetail

urlpatterns = [
    path('brands/', BrandList.as_view()),  # URL pattern for listing all brands
    path('brands/<slug:slug>/', BrandDetail.as_view()),  # URL pattern for a specific brand
    path('', ProductList.as_view()),  # URL pattern for the product list
    path('<slug:slug>', ProductDetail.as_view()),  # URL pattern for a specific product
]
