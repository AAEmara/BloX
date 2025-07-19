from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from .forms import UserForm, CustomLoginForm


def register_view (request):
    if request.user.is_authenticated:
        return redirect('blog:home')

    # if the request is POST we will take the data and validate it 
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful! Please log in.')
            # when implement the login.html we will redirect the user to login
            return redirect('blog_auth:login')
    else:
        form = UserForm()
    register_form = {'form': form}
    # when implement the register.html we will render it
    return render(request, 'blog_auth/register.html', context=register_form)


def login_view (request):

    if request.user.is_authenticated:
        return redirect('blog:home')

    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            if request.GET.get('next') is not None:
                return redirect(request.GET.get('next'))
            return redirect('blog:home')
    else:
        form = CustomLoginForm()
    login_form = {'form': form}
    return render(request, 'blog_auth/login.html',context=login_form)


def logout_view(request):
    logout(request)
    return redirect('blog:home')
