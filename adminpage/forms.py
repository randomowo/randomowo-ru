"""
"""
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length= 25,label="username")
    password = forms.CharField(max_length= 30, label='password', widget=forms.PasswordInput)
