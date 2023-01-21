from django.db import models
from django.contrib.contenttypes.models import ContentType

from users.models import User
from shop.models import Product



class CartUser(models.Model):
    user = models.OneToOneField(to=User, related_name="cartUser", verbose_name="Пользователя", on_delete=models.CASCADE, null=True)
    pcart = models.JSONField(null=True)
    
    
