"""
"""
import random

from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import render


def yesno(request):
    """
    """
    template_name = "user/yesno.html"
    context = {
        "answer": random.choice(["YES", "NO"]),
    }
    return render(request, template_name, context)
