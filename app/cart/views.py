from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.generic.edit import BaseFormView
from django.views.generic import TemplateView, FormView
from shop.models import *
from .forms import CartAddProductForm
from .cart import Cart
from django.core import serializers
from .models import *
from users.models import User


class AddCart(FormView):
    form_class = CartAddProductForm
    
    def post(self, request, product_id):
        cart = Cart(self.request)
        form = self.form_class(self.request.POST)
        product = get_object_or_404(Product, id=product_id)
        context= Product.objects.filter(id=product_id).values('id','name', 'image', 'price')[0]
        if form.is_valid():
            cd = form.cleaned_data
            cart.add(product=product, quantity=cd["quantity"], update_quantity=cd['update'])
        
        data = {
            "id" : context['id'],
            'name' : context['name'],
            "image" :  'media/' + context['image'],
            "price" : context['price'],
        }
        user = CartUser.objects.filter(user=self.request.user)
        user.update(pcart=self.request.session['cart'])

        return render(request, "cart/cartProduct.html", context=data)
        
class RemoveCart(FormView):
    def post(self, request, product_id):
        
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        cart.remove(product)
        
        user = CartUser.objects.filter(user=self.request.user)
        user.update(pcart=self.request.session['cart'])
                
        
        
     
        return JsonResponse({'data':"Удаленно"})

