import json
from django.http import Http404, HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView, FormView, DetailView
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
    
class ShopView(ListView):
    template_name = 'shop/shop.html'
    context_object_name = 'products'

    
    def get_context_data(self ,*args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['searchForm'] = SearchForm()
        context['title'] = 'Магазин'
        context['cat'] = Category.objects.all()
        context['cat_selected'] = 0
        
        return context
    
    def get_queryset(self):
        return Product.objects.all()
    

class CategoryView(ListView):
    template_name = 'shop/shop.html'
    context_object_name = 'products'
    
    
    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs['slug_cat'])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категория'
        context['searchForm'] = SearchForm()
        context['cat_selected'] = self.kwargs['slug_cat']
        context['cat'] = Category.objects.all()
        return context
    
class ProductView(DetailView):
    model = Product
    template_name = 'shop/detailProduct.html'
    slug_url_kwarg = 'slug_product'
    context_object_name = 'product'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.kwargs['slug_product']
        return context
    