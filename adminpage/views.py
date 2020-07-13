"""
"""
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect

from adminpage.forms import LoginForm


def loginpage(request):
    """
    """
    template_name = "admin/login.html"
    form = LoginForm(request.POST or None)
    context = {
        "form": form,
    }
    if form.is_valid():
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(request.POST.get("next") or "/admin/")
        else:
            messages.error(request, "username/password incorrect")
    return render(request, template_name, context)

def logoutpage(request):
    """
    """
    logout(request)
    return redirect(request.GET.get("next", "/"))
