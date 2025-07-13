from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class UserForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered")
        return email
    
    def clean(self):

        # this is to do the clean function in the UserCreationForm to get the cleaned (validated) data
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirmation = cleaned_data.get('password2')
        if (password and password_confirmation) and (password != password_confirmation):
            raise forms.ValidationError("Passwords don't match.")
        
        return cleaned_data
        