import json
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView, FormView
from django.template.loader import render_to_string
from .models import *
from users.forms import *
from .forms import *
# Create your views here.

class IndexShow(TemplateView):
    template_name = "index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Succulentum'
        return context
    


class SearchView(FormView):
    def post(self, request):
        form = SearchForm(request.POST)
        search = []
        if form.is_valid():
            search = form.cleaned_data
            
        return HttpResponse(search) 
    
class ShopView(TemplateView):
    template_name = 'shop/shop.html'
    

    
    def get_context_data(self ,*args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['searchForm'] = SearchForm()
        context['title'] = 'Магазин'
        return context
    

    
    
    