"""
"""
from challenges.models import Challenge
from django.shortcuts import render
from filmlist.models import Film


def film_list(request):
    """
    """
    films = Film.objects.all()
    template_name = "index.html"
    context = {
        "page": "flist",
        "films": films,
    }
    return render(request, template_name, context)


def random_film(request):
    """
    """
    film = Film.objects.filter(is_watched=False).order_by("?").first()
    template_name = "index.html"
    context = {
        "page": "random",
        "film": film,
    }
    return render(request, template_name, context)
