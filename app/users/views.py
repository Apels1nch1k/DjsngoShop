from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.contrib.auth.views import LogoutView, LoginView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, FormView
from django.contrib.auth import authenticate, login
from .forms import *

class SingUpView(CreateView):
    form_class = SingUpForms
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            authenticate(self.request,username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            form.save()
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
            return JsonResponse({'success': 'ok'})
        else:
            return JsonResponse({'errors': form.errors })
