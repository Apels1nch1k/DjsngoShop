from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(CartUser)
class CartUserAdmin(admin.ModelAdmin):
    pass

