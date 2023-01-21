from django.urls import path, include

from .views import *

app_name = 'orders'

urlpatterns = [
    path('create/',  CreateOrder.as_view(), name="create"),

]