from django.contrib import admin

# Register your models here.
from .models import Address, Profile,ContactNumbers
admin.site.register(Profile)
admin.site.register(ContactNumbers)
admin.site.register(Address)