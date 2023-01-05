from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.validators import RegexValidator
from django.forms import ValidationError
from .models import User

class SingUpForms(UserCreationForm):
    fio= forms.CharField(
        widget=forms.TextInput(attrs={'autocomplete': 'text', 'placeholder': 'Введите ФИО', 'class':'agreedInput'}),
        required=False,
        validators=[RegexValidator(r'([А-ЯЁ][а-яё]+[\-\s]?){3,}', "Введите ФИО кириллицой")]
        
    )
    username =  forms.CharField(
        widget=forms.TextInput(attrs={'autocomplete': 'text', 'placeholder': 'Введите логин', 'class':'agreedInput'}),
        required=False,
        validators=[RegexValidator(r'[^0-9а-яА-ЯёЁ]', "Введите логин латиницой")],
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'autocomplete': 'email','placeholder': 'Введите электрону почту ', 'class':'agreedInput' }),
        required=False
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={ 'placeholder': 'Введите пароль ', 'class':'agreedInput'}),
        required=False
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Повторите пароль', 'class':'agreedInput'}),
        required=False
    )
    
    
    def clean_password1(self):
        password = self.cleaned_data['password1']
        if password == '':
            raise ValidationError('Введите пароль', code='invalid')
        return password 
    def clean_username(self):
        username = self.cleaned_data['username']
        if username == '':
            raise ValidationError('Введите логин ', code='invalid')
        return username
    def clean_fio(self):
        fio = self.cleaned_data['fio']
        if fio == '':
            raise ValidationError('Введите ФИО', code='invalid')
        return fio
    def clean_email(self):
        email = self.cleaned_data['email']
        if email == '':
            raise ValidationError('Введите электроную почту', code='invalid')
        return email
    
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("fio","username", "email", "password1", "password2")
        


class SingInForms(AuthenticationForm):
    username = forms.CharField(
        label=(""),
        max_length=254,
        widget=forms.TextInput(
            attrs={
                'autocomplete': 'text',
                'placeholder': 'Логин',
                'class': 'agreedInput',
            }
        ),
        required=False
    )
    password = forms.CharField(
        label=(""),
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "current-password",
                'placeholder': 'Пароль',
                'class': 'agreedInput',
            }
        ),
        required=False
    )
    
    error_messages = {
        "invalid_login": (
            "Введите логин и пароль правильно"
        ),
    }
    

    def clean_password(self):
        password = self.cleaned_data['password']
        if password == '':
            raise ValidationError('Введите пароль', code='invalid')
        return password 
    def clean_username(self):
        username = self.cleaned_data['username']
        if username == '':
            raise ValidationError('Введите логин ', code='invalid')
        if not User.objects.filter(username=username):
            raise ValidationError('Такого пользователя не существует', code='invalid')
        return username

    
    