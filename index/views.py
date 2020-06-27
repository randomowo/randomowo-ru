"""
"""
from bestmoments.views import best_image_list
from challenges.views import challenge_list
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import render
from filmlist.views import film_list
from filmlist.views import random_film
from wishlist.views import wish_list
import random


def index_page(request):
    """
    """
    if request.method == "POST":
        if "chlist" in request.POST:
            return challenge_list(request)
        elif "flist" in request.POST:
            return film_list(request)
        elif "wlist" in request.POST:
            return wish_list(request)
        elif "bmoments" in request.POST:
            return best_image_list(request)
        elif "random" in request.POST or "random_choice" in request.POST:
            return random_film(request)
    else:
        return film_list(request)

def yesno(request):
    """
    """
    template_name = "user/yesno.html"
    context = {
        "answer": random.choice(["YES", "NO"]),
    }
    return render(request, template_name, context)

@login_required
def admin_index_page(request):
    pass
