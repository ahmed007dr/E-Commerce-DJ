from django.contrib import admin

# Register your models here.
from .models import Product , Brand , ProductImages ,Review


class ProductImagesInLine(admin.TabularInline):
    model = ProductImages  # استخدم الاسم الصحيح للموديل

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImagesInLine]  # إضافة الـ inlines لعرض الصور داخل المنتج
    search_fields = ['name', 'flag', 'price', 'sku']  # حقول البحث في واجهة المنتج
    extra = 1  # عدد الصفوف الإضافية التي تظهر بشكل افتراضي



admin.site.register(Product,ProductAdmin)
admin.site.register(Brand)
admin.site.register(Review)