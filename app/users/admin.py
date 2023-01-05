from django.contrib import admin

from .models import *
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'fio')
    list_display_links = ('id', 'fio')
    search_fields = ('id', 'fio')
    
    
admin.site.register(User, UserAdmin)