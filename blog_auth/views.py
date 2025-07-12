from django.shortcuts import render, redirect
from .forms import UserForm
# Create your views here.

def user_register (request):
    if request.user.is_authenticated:
        redirect('home')

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
