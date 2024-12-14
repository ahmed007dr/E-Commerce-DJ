from django.contrib import admin

# Register your models here.
from .models import Product , Brand , ProdcutImages ,Review


class ProductImagesInLine(admin.TabularInline):
    model = ProdcutImages  # استخدم الاسم الصحيح للموديل

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImagesInLine]  # إضافة الـ inlines لعرض الصور داخل المنتج



admin.site.register(Product,ProductAdmin)
admin.site.register(Brand)
admin.site.register(Review)