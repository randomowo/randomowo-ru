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
