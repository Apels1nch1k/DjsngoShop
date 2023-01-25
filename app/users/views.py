from django.shortcuts import redirect
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.contrib.auth.views import LogoutView, LoginView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, FormView
from django.contrib.auth import authenticate, login
from django.views.generic import TemplateView, ListView, FormView
from orders.models import Order, OrderProduct

from cart.models import CartUser
from .forms import *

class SingUpView(CreateView):
    form_class = SingUpForms
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            form.save()
            user = User.objects.get(username=form.cleaned_data['username'])
            CartUser.objects.create(user=user)
            return JsonResponse({'success': 'ok'})
        else:
            print(form.cleaned_data)
            return JsonResponse({'errors': form.errors})
        
        
class SingInView(LoginView):
    form_class = SingInForms
    def post (self, request):
        form = self.form_class(data =request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            self.request.session['cart'] = CartUser.objects.get(user=user).pcart
            
            return redirect(reverse_lazy('shop:home'))
        else:
            return JsonResponse({'errors': form.errors })




class Logout(LogoutView):
    pass



class Profil(ListView):
    template_name = "profil/profil.html"
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Профиль"
        # context['userOrder'] = Order.objects.get(user=self.request.user)
        # context['orderProduct'] = OrderProduct.objects.filter(order=Order.objects.get(user=self.request.user))
        return context
    
    def get(self, request, *args, **kwargs) :
        userOrder = Order.objects.filter(user=self.request.user)

        
        
        context = {
            'userOrder': userOrder,
        }
        
        return render(request, self.template_name, context)
    