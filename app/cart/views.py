import json
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.http.response import HttpResponseBase
from django.views import View
from django.views.generic.edit import BaseFormView, BaseDeleteView
from django.views.generic import TemplateView, FormView, CreateView, DeleteView
from shop.models import *
from .cart import Cart
from .models import *

class AddCart(CreateView):
    
    def post(self, request, product_id):
        cart = Cart(self.request)
        quantity = self.request.POST.get('quantity')
        product = get_object_or_404(Product, id=product_id)
        context= Product.objects.filter(id=product_id).values('id','name', 'image', 'price')[0]

        cart.add(product=product, quantity=int(quantity), update_quantity=int(quantity))
        number_in_cart : len(self.request.session['cart'])  =  0
        print(number_in_cart)
        data = {
            "id" : context['id'],
            'name' : context['name'],
            "image" :  '/media/' + context['image'],
            "price_total" : int(context['price']) * int(self.request.session['cart'][str(product_id)]['quantity']),
            "quantity": self.request.session['cart'][str(product_id)]['quantity'],
            "all_price_total" :  cart.get_total_price(),
            "number": number_in_cart

        }
        
        if self.request.user.is_authenticated:
            user = CartUser.objects.filter(user=self.request.user)
            user.update(pcart=self.request.session['cart'])
        return render(request, "cart/cartProduct.html", context=data)
        
class RemoveCart(View):
    http_method_names = ['post']
    
    def post(self, request, product_id):
        cart = Cart(self.request)
        
        product = get_object_or_404(Product, id=product_id)
        cart.remove(product)
        number_in_cart =  len(self.request.session['cart']) | 0
        if self.request.user.is_authenticated:
            user = CartUser.objects.filter(user=self.request.user)
            user.update(pcart=self.request.session['cart'])
        return render(request, 'none.html',   status=200)
        



class UpdateCart(FormView):
    def post(self, request, product_id):
        cart = Cart(self.request)
        quantity = self.request.POST.get('quantity')
        print(quantity)
        product = get_object_or_404(Product, id=product_id)
        context= Product.objects.filter(id=product_id).values('id','name', 'price')[0]

        cart.add(product=product, quantity=int(quantity), update_quantity=int(quantity))
        # cart_price = [ i for i in cart.session]
        # print([i for i in cart_price] )

        number_in_cart : 0 =  len(self.request.session['cart']) 
        data = {
            "id" : context['id'],
            'name' : context['name'],
            "price_total" : int(context['price']) * int(self.request.session['cart'][str(product_id)]['quantity']),
            "quantity": self.request.session['cart'][str(product_id)]['quantity'],
            "all_price_total" :  cart.get_total_price(),
            "number": number_in_cart,
        }
        print(self.request.session['cart'])
        if self.request.user.is_authenticated:
            user = CartUser.objects.filter(user=self.request.user)
            user.update(pcart=self.request.session['cart'])
            
        print(data)
        return JsonResponse(data=data)