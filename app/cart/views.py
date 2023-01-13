from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.generic.edit import BaseFormView
from django.views.generic import TemplateView, FormView
from shop.models import *

import json

# class Cart(TemplateView):
#     template_name = "cart.html"
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         return context
    
    
class AddCart(FormView):
    
    
    def post(self, request, id):
        if not request.session.get('cart'):
            request.session['cart'] = list()
        else:
            request.session['cart'] = list(request.session['cart'])
        product_exist = next((product for product in request.session['cart'] if product["type"] == request.POST.get('type') and product['id'] == int(id)), False)
        

        add_data = {
            'id': int(id),
            'type': request.POST.get('type'),
            'name': request.POST.get('name'),
            'image': request.POST.get('image'),
            'price': request.POST.get('price'),
            'numberCArt': len(self.request.session['cart'])
        }
        print(add_data)
        # print( [i['id'] for i in  request.session['cart']])
        if not product_exist:
            request.session['cart'].append(add_data)
            request.session.modified = True
        
        return render(request, "cartProduct.html", context=add_data)
        
class RemoveCart(FormView):
    def post(self, request, id):
        for product in self.request.session['cart']:
            if product['id'] == int(id):
                product.clear()
                      
        while {} in self.request.session['cart']:
            self.request.session['cart'].remove({})
        
        if not self.request.session['cart']:
            del self.request.session['cart']
            
            
        request.session.modified = True
     
        return JsonResponse({'data':"Удаленно"})

    