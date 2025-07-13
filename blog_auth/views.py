from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm, LoginForm
# Create your views here.

def user_register (request):
    if request.user.is_authenticated:
        return redirect('home')

    # if the request is POST we will take the data and validate it 
    if request.method == 'POST':
        register_form = UserForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            # when implement the login.html we will redirect the user to login
            # return redirect('login')
    else:
        register_form = UserForm()
    context = {'register_form': register_form}
    # when implement the register.html we will render it
    # return render(request, 'register.html', context=context)

def user_login (request):

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            if request.GET.get('next') is not None:
                return redirect(request.GET.get('next'))
            
            return redirect('home')
    else:
        form = LoginForm()
    context = {'form': form}
    # return render(request, 'login.html',context=context)

def user_logout(request):
    logout(request)
    # return redirect('blog_auth:login')
    # return redirect('blog_auth:login')
