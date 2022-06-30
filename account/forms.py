from django import forms
from django.forms import ModelForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth import authenticate


class CreateUser(UserCreationForm):
    first_name = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class':'text-input', 'placeholder':'First Name'}),
    )
    last_name = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class':'text-input', 'placeholder':'Last Name'}),
    )
    email = forms.EmailField(
        required=False,
        widget=forms.EmailInput(attrs={'class':'text-input', 'placeholder':'Enter your Email'}),
    )

    username = forms.CharField(
        widget=forms.TextInput(attrs={'class':'text-input', 'placeholder':'Enter your username'}),
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'text-input', 'placeholder':'Enter your password'}),
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'text-input', 'placeholder':'Confirm password'}),
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username' , 'password1', 'password2']

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already taken")
        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists() and email !="":
            raise forms.ValidationError("Email is already used")
        return email

class UserEditForm(forms.ModelForm):
    first_name = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class':'text-input', 'placeholder':'First Name'}),
    )
    last_name = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class':'text-input', 'placeholder':'Last Name'}),
    )
    email = forms.EmailField(
        required=False,
        widget=forms.EmailInput(attrs={'class':'text-input', 'placeholder':'Enter your Email'}),
    )
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')



class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('image',)

