from django.contrib import admin

# Register your models here.
from .models import Settings ,Locations, DeliveryFee

class DeliveryFeeInline(admin.TabularInline):  
    model = DeliveryFee
    extra = 1  
    fields = ('fee',)  

class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'details_name')  
    search_fields = ('name', 'details_name')  
    list_filter = ('name',)  
    inlines = [DeliveryFeeInline]  

admin.site.register(Locations, LocationAdmin)
admin.site.register(Settings)
