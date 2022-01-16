from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from htmlmin.decorators import minified_response

# Create your views here.
# login de usuario
@minified_response
def login_user(request):
    return render(request, 'login.html',
        {
            'title':'iheal - Login',
        }                          
    )
    
@minified_response
def logout_user(request):
    logout(request)
    return redirect ('/')
    
# processamento do login de usuario
@minified_response
def submit_login(request):
    
    if request.POST:
        username = request.POST.get('login-email')
        password = request.POST.get('login-password')
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Usuario ou senha invalidos!')
            
        return redirect('/')

# login obrigado
@minified_response
@login_required(login_url='/login/')
def home(request):
    return render(request, 'home.html',
        {
            'title':'iheal - Home',
        }
    )
