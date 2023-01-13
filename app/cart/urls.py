from django.urls import path, include

from .views import *

app_name = 'cart'

urlpatterns = [
    # path('',  Cart.as_view(), name="cart"),
    path('add/<id>/',  AddCart.as_view(), name="addcart"),
    path('remove/<id>/',  RemoveCart.as_view(), name="removecart"),

]