from django.contrib import admin

# Register your models here.
from .models import Product , Brand

admin.register.site(Product)
admin.register.site(Brand)