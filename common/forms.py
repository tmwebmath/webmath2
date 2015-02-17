from django import forms
from django.forms.extras.widgets import *

# pour supprimer les doubles points dans les formulaires générés, : https://github.com/torchbox/wagtail/issues/130

class LoginForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    username = forms.CharField(label='Ton nom', widget= forms.TextInput(attrs={'class' : 'form-control'}))
    password = forms.CharField(label='Ton mot de passe', widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
    confirm_password = forms.CharField(label='Confirmation de ton mot de passe', widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
    mail = forms.CharField(label='Ton E-mail', widget=forms.EmailInput(attrs={'class' : 'form-control'}))