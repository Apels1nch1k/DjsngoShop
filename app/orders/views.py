from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView, CreateView
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect
from cart.cart import Cart
from .forms import OrderCreateForm
from .models import OrderProduct

class CreateOrder(CreateView):
    form_class = OrderCreateForm
    template_name = "orders/orders.html"
    
    def post(self, request):
        cart = Cart(self.request)
        form = OrderCreateForm(self.request.POST)
        print(self.request.user)
        if form.is_valid():
            
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            for i in cart:
                OrderProduct.objects.create(
                    order=order,
                    product=i['product'],
                    price=i['price'],
                    quantity=i['quantity'],
                )
            cart.clear()
        return redirect(reverse_lazy('shop:home'))
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Оформление заказа'
        context['formOrder'] = self.form_class
        return context
        
    
    