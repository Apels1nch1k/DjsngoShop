from users.forms import *
from django.contrib.auth.views import LogoutView
from shop.models import Product
from cart.forms import CartAddProductForm
from cart.cart import Cart

def singup(request):
    return {'formsingup': SingUpForms(),}

def singin(request):
    return {'formsingin': SingInForms(),}

def product(request):
    return {'products' : Product.objects.all()}

def addcart(request):
    return {'addcart' : CartAddProductForm(), }

def updateCart(request):
    cart = Cart(request)
    
    # for item in cart:
    #     item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update' : True})
    
    return {'cart' : cart, }
