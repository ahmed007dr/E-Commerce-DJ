from .views import ProductList , ProductDetail ,BrandList,BrandDetail
from django.urls import path


urlpatterns = [
    path('brand/',BrandList.as_view()),
    path('brand/<slug:slug>/',BrandDetail.as_view(), name='brand_detail'),

    path('',ProductList.as_view()),
    path('<slug:slug>',ProductDetail.as_view()),

] 