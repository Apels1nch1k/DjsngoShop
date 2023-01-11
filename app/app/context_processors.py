from users.forms import *
from django.contrib.auth.views import LogoutView
from shop.models import Product
def singup(request):
    return {'formsingup': SingUpForms(),}

def singin(request):
    return {'formsingin': SingInForms(),}

def product(request):
    return {'products' : Product.objects.all()}
