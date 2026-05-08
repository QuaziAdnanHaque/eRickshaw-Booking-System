from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    user_type = forms.ChoiceField(choices=[
        ('customer', 'Customer'),
        ('driver', 'Driver'),
    ])
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

# Quazi@admin