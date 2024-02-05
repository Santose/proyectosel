from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from mainapp.formulario import RegisterForm 
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def index(request):
    return render(request, 'mainapp/index.html', {'title':'inicio'})

def about(request):
    return render(request, 'mainapp/about.html', {'about':'A cerca de nosotros'})

def register_page(request):
    if request.user.is_authenticated:
        return redirect('index')
    
    #register_form = UserCreationForm()  # la que trae pos default django
    register_form = RegisterForm() # la adaptada por nosotros
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request,'Te has registrado correctamente')
            return redirect('index')

    return render(request, 'users/register.html',{
        'title': 'Registro',
        'register_form': register_form
    })

def login_page(request):
    
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            messages.warning(request, 'Identificacion erronea')


    return render(request, 'users/login.html', {
        'title': 'Login de usuario'
    })

def logout_user(request):
    logout(request)
    return redirect('index')
