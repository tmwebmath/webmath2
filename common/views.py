from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from common.forms import LoginForm, RegisterForm
from django.core.urlresolvers import reverse
from common.models import *
from django.contrib.auth.models import User

def connexion(request):
    erreur = False
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
            else:
                erreur = True
    else:
        form = LoginForm()
        
    return render(request, "common/login.html", locals())
    
def deconnexion(request):
    logout(request)
    return redirect('common:connexion')
    
    
def register(request):
    if request.method == "POST":
        registerform = RegisterForm(data=request.POST)
        
        if registerform.is_valid():
            username = registerform.cleaned_data["username"]
            password = registerform.cleaned_data["password"]
            confirm_password = registerform.cleaned_data["confirm_password"]
            mail = registerform.cleaned_data["mail"]
            
            if password == confirm_password:
                user = User.objects.create_user(username, mail, password)
                user.save()
                
                student = Student()
                student.user = user
                student.save()
            
    else:
        registerform = RegisterForm()
        
    return render(request, "common/register.html", {'registerform' : registerform})
    