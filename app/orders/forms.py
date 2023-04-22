from django import forms

from .models import Order

class OrderCreateForm(forms.ModelForm):
    address = forms.CharField(widget=forms.TextInput(
        attrs={
            'class' : 'orderForm',
            'placeholder' : "Адрес",
        }
        
    ))
    city = forms.CharField(widget=forms.TextInput(
        attrs={
            'class' : 'orderForm',
            "placeholder" : "Город",
        }
        
    ))
    
    
    class Meta:
        model = Order
        fields = ['address', 'city']