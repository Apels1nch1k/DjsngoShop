from users.forms import *
from django.contrib.auth.views import LogoutView
from shop.models import Product
from cart.cart import Cart

def singup(request):
    return {'formsingup': SingUpForms(),}

def singin(request):
    return {'formsingin': SingInForms(),}



def cart(request):

    return {'cart' : Cart(request), }
