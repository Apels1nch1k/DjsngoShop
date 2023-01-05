from users.forms import *
from django.contrib.auth.views import LogoutView

def singup(request):
    return {'formsingup': SingUpForms(),}

def singin(request):
    return {'formsingin': SingInForms(),}
