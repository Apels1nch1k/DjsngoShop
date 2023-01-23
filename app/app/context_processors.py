from users.forms import *
from django.contrib.auth.views import LogoutView
from shop.models import Product
from cart.forms import CartAddProductForm
from cart.cart import Cart

def singup(request):
    return {'formsingup': SingUpForms(),}

def singin(request):
    return {'formsingin': SingInForms(),}


def addcart(request):
    return {'addcart' : CartAddProductForm(), }

def updateCart(request):

    return {'cart' : Cart(request), }
