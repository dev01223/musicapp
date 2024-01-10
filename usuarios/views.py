from django.shortcuts import render
from usuarios.forms import *
from .models import *
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth import login as auth_login
from .forms import LoginForm
from django.contrib.auth import authenticate
import logging
import googlemaps
from django.contrib import messages



# Create your views here.
# Create your views here.
def register(request):
    form = ClienteRegistrationForm()

    if request.method == 'POST':
        form = ClienteRegistrationForm(request.POST, request.FILES)
        
        if form.is_valid():
           
                user = CustomUser.objects.create_user(
                    username = form.cleaned_data['username'],
                    email=form.cleaned_data['email'],
                    password=form.cleaned_data['password1'],
              
                 
                  
                )
                user.save()

             
               
               
                    
                messages.success(request, 'Cadastro Realizado com sucesso!')
                return redirect('login')
        else:
            print("Formulário inválido")
            messages.error(request, form.errors)
    
    return render(request, 'core/registro.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        
        if user is not None:
            if user.first_login is None:
                user.first_login = timezone.now()
            user.save()  # Salva a alteração no banco de dados
            auth_login(request, user)
            messages.success(request, "Usuário logado com sucesso!")
            return redirect('home')
        else:
            messages.error(request, "Email ou senha inválidos.")
    else:
        form = LoginForm()
        
        
    return render(request, 'core/login.html')

