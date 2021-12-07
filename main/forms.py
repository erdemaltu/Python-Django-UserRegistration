from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'UserName'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'Password'
    }))


tuple_of_gender= [('MALE','MALE'),('FEMALE','FEMALE')]

class SignUpForm(UserCreationForm):
    
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'First Name'
    }))

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Last Name'
    }))

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'User Name'
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class':'form-control',
        'placeholder':'Email'
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'Password'
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'Re-Type Password'
    }))
    
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2', )


class AccountForm(SignUpForm):

    gender = forms.ChoiceField(choices=tuple_of_gender, widget=forms.Select(attrs={
        'class':'form-control',
        'placeholder':'Gender'
    }))
    
    phone = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Phone'
    }))
    
    address = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Address'
    }))
