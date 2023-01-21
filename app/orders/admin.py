from django.contrib import admin
from .models import *



class OrderProductAdmin(admin.TabularInline):
    model = OrderProduct
    raw_id_fields = ['product']
    
    
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'address', 'city', 'paid',
                    'created', 'updated']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderProductAdmin]
    