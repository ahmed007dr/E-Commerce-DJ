from .views import ProductList , ProductDetail
from django.urls import path


urlpatterns = [
    path('',ProductList.as_view()),
    path('<slug:slug>',ProductDetail.as_view()),

] 