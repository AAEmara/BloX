import threading
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from .forms import UserForm, CustomLoginForm
from django.conf import settings
from .models import CustomUser


# --- Asynchronous Email Sending Helper ---
def send_welcome_email_async(user_id, user_email, username):
    
    try:
        user = CustomUser.objects.get(pk=user_id)
        subject = 'Welcome to Our Blog!'
        plain_message = f'Hi {user.username},\n\nWelcome to our blog! We are excited to have you.\
            \n\nBest regards,\nYour Blog Team'

        from_email = settings.DEFAULT_FROM_EMAIL if hasattr(settings, 'DEFAULT_FROM_EMAIL') else 'webmaster@localhost'
        recipient_list = [user_email]

        send_mail(
            subject,
            plain_message, # Only provide the plain text message
            from_email,
            recipient_list,
            fail_silently=False,
        )
        print(f"Welcome email sent successfully to {user_email}")
    except Exception as e:
        print(f"Error sending welcome email to {user_email}: {e}")

# --- END NEW: Asynchronous Email Sending Helper ---

def register_view (request):
    if request.user.is_authenticated:
        return redirect('blog:home')

    # if the request is POST we will take the data and validate it 
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()

            # --- NEW: Dispatch Welcome Email Asynchronously ---
            # Pass necessary user data to the async function
            email_thread = threading.Thread(
                target=send_welcome_email_async,
                args=(user.pk, user.email, user.username) # Pass user ID, email, username
            )
            email_thread.daemon = True # Allow the main program to exit even if thread is running
            email_thread.start()
            # --- END NEW: Dispatch Welcome Email Asynchronously ---

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
