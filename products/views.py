from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render , redirect
from django.views.generic import ListView,DetailView
# Create your views here.
from .models import Product , Brand , Review ,ProductImages
from django.shortcuts import get_object_or_404

from django.db.models.aggregates import Count



class ProductList(ListView):
    model = Product
    paginate_by = 20

class ProductDetail(DetailView):
    model = Product
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # Get the default context with the product object
        context['reviews'] = Review.objects.filter(product=self.get_object())  # Add reviews to context
        context['images'] = ProductImages.objects.filter(product=self.get_object())  # Fix typo here
        context['related'] = Product.objects.filter(brand=self.get_object().brand)[:10]
        return context
    

class BrandList(ListView):
    model = Brand
    paginate_by = 20
    queryset = Brand.objects.annotate(product_count=Count('product_brand'))# related_name = ' product_brand' === class product

class BrandDetail(ListView):
    model = Product
    template_name = 'products/brand_detail.html'
    paginate_by = 20

    def get_queryset(self):
        # Ensure we're fetching the correct brand based on the slug
        brand = get_object_or_404(Brand, slug=self.kwargs['slug'])
        # Return products that belong to this brand
        return Product.objects.filter(brand=brand)[:10]

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     # Add the brand to the context so we can display its name and details
    #     context['brand'] = get_object_or_404(Brand, slug=self.kwargs['slug']).annotate(product_brand=Count('product_brand'))[0]
    #     return context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # الحصول على الكائن الصحيح من العلامة التجارية باستخدام slug
        brand = get_object_or_404(Brand, slug=self.kwargs['slug'])
        # استخدام annotate للحصول على عدد المنتجات المرتبطة بالعلامة التجارية
        brand_with_count = Brand.objects.annotate(product_count=Count('product_brand')).get(slug=self.kwargs['slug'])
        
        context['brand'] = brand_with_count
        return context


# class BrandDetail(DetailView):
#     model = Brand
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)  
#         context['products'] = Product.objects.filter(brand = self.get_object())

#         return context

def add_review(request,slug):
    product = Product.objects.get(slug=slug)
    review = request.POST['review'] 
    rate = request.POST['rate']
    # Calculate average rating or get the first review's rating for demonstration

    Review.objects.create(
        user = request.user,
        product = product ,
        review = review ,
        rate = rate
    )
    return redirect(f'/products/{slug}')