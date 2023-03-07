from django import forms
from .views import *
from django.contrib.auth.models import User
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, PasswordChangeForm


class RestauranteFormulario(forms.Form):
    plato=forms.CharField(label="Plato", max_length=40)
    cantidad=forms.CharField(label="Cantidad", max_length=20)
    bebida=forms.CharField(label="Bebida", max_length=40)
    numero_de_mesa=forms.CharField(label="Numero de Mesa", max_length=5)

class EntradaFormulario(forms.Form):
    plato=forms.CharField(label="Plato", max_length=40)
    cantidad=forms.CharField(label="Cantidad", max_length=20)
    bebida=forms.CharField(label="Bebida", max_length=40)
    numero_de_mesa=forms.CharField(label="Numero de Mesa", max_length=5)

class UserRegisterForm(UserCreationForm):
    email= forms.EmailField
    password= forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)
    last_name= forms.CharField()
    first_name= forms.CharField()

    class Meta:
        model= User
        fields=  ["username", "email", "password", "password2", "last_name", "first_name"]
        help_texts= {k:"" for k in fields}

class UserEditForm(UserCreationForm):
    email= forms.EmailField(label="Modificar Email")
    password= forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)

    last_name=forms.CharField
    first_name=forms.CharField

    class meta:
        model= User
        fields=  ["username", "email", "password", "password2", "last name", "first name"]
        help_texts= {k:"" for k in fields}

class FormularioCambioPassword(PasswordChangeForm):
    old_password = forms.CharField(label=("Password Actual"),widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password1 = forms.CharField(label=("Nuevo Password"), widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password2 = forms.CharField(label=("Repita Nuevo Password"), widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')


#class RegisterForm(UserCreationForm):
    # fields we want to include and customize in our form
    first_name = forms.CharField(max_length=100, required=True,widget=forms.TextInput(attrs={'placeholder': 'First Name','class': 'form-control', }))
    last_name = forms.CharField(max_length=100, required=True,widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'class': 'form-control', }))
    username = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control', }))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Email','class': 'form-control',}))
    password1 = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control','data-toggle': 'password','id': 'password',}))
    password2 = forms.CharField(max_length=50, required=True,widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 'class': 'form-control','data-toggle': 'password', 'id': 'password', }))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

#class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'placeholder': 'Username','class': 'form-control',}))
    password = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control', 'data-toggle': 'password','id': 'password', 'name': 'password',}))
    remember_me = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['username', 'password', 'remember_me']