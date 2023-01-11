from django.contrib import admin
from .models import *

from django.utils.safestring import mark_safe
# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )}
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'image_show', 'price', 'created', 'uploaded']
    list_filter = ['name', 'uploaded', 'created']
    prepopulated_fields = {'slug': ('name', )}
    readonly_fields = ('created', 'uploaded')
    def image_show(self, obj):
        return mark_safe(f"<img src='{obj.image.url}' width='60' />")
    
    image_show.short_description = "Фотография"