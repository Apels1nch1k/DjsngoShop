from django.urls import path, include

from .views import *

app_name = 'shop'

urlpatterns = [
    path('',  IndexShow.as_view(), name="home"),
    path('shop',  ShopView.as_view(), name="shop"),
    path('search',  SearchView.as_view(), name="search"),
    path('category/<slug:cat_slug>',  CategoryView.as_view(), name="category"),
]