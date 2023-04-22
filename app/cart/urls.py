from django.urls import path, include

from .views import *

app_name = 'cart'

urlpatterns = [
    path('add/<int:product_id>/',  AddCart.as_view(), name="addcart"),
    path('remove/<int:product_id>',  RemoveCart.as_view(), name="removecart"),
    path('update/<int:product_id>/',  UpdateCart.as_view(), name="update"),
    

]