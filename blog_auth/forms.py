from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class UserForm(UserCreationForm):

    email = forms.EmailField(
        required = True,
        widget = forms.EmailInput(attrs = {
            'class': 'form-control',
            'placeholder': 'Enter your email'
        })
    )
    username = forms.CharField(
        required = True,
        widget = forms.TextInput(attrs = {
            'class': 'form-control',
            'placeholder': 'Choose a username'
        })
    )
    first_name = forms.CharField(
        required = True,
        widget = forms.TextInput(attrs = {
            'class': 'form-control',
            'placeholder': 'First name'
        })
    )
    last_name = forms.CharField(
        required = True,
        widget = forms.TextInput(attrs = {
            'class': 'form-control',
            'placeholder': 'Last name'
        })
    )
    password1 = forms.CharField(
        label = "Password",
        required = True,
        widget = forms.PasswordInput(attrs = {
            'class': 'form-control',
            'placeholder': 'Enter a password'
        })
    )
    password2 = forms.CharField(
        label = "Confirm Password",
        required = True,
        widget = forms.PasswordInput(attrs = {
            'class': 'form-control',
            'placeholder': 'Confirm your password'
        })
    )


    class Meta:
        model = CustomUser
        fields = (
            'username', 'email', 'first_name',
            'last_name', 'password1', 'password2')


    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered.")
        return email


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        label = 'Username',
        widget = forms.TextInput(attrs = {
            'class': 'form-control',
            'placeholder': 'Enter your username'
        })
    )
    password = forms.CharField(
        label = 'Password',
        widget = forms.PasswordInput(attrs = {
            'class': 'form-control',
            'placeholder': 'Enter your password'
        })
    )


    def confirm_login_allowed(self, user):
        if user.is_blocked:
            raise forms.ValidationError(
                "Sorry, you are blocked. Contact the admin.",
                code = "blocked",
            )
