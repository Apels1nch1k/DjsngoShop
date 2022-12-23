from django.urls import path, include

from .views import *

urlpatterns = [
    path('',  IndexShow.as_view(), name="home"),
]