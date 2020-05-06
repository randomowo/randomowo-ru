"""
"""
from challenges.models import Challenge
from django.shortcuts import render
from filmlist.forms import RandomForm
from filmlist.models import Film


def film_list(request):
    """
    """
    films = Film.objects.order_by("is_watched")
    watched = films.filter(is_watched=True).count()
    template_name = "user/index.html"
    context = {
        "page": "flist",
        "films": films,
        "films_watched": watched,
        "films_count": films.count(),
    }
    return render(request, template_name, context)


def random_film(request):
    """
    """
    filter_choice = (request.POST["filter_choice"]
                     if "filter_choice" in request.POST else "unwatched")
    if filter_choice == "all":
        film = Film.objects.all().order_by("?").first()
    elif filter_choice == "watched":
        film = Film.objects.filter(is_watched=True).order_by("?").first()
    elif filter_choice == "unwatched":
        film = Film.objects.filter(is_watched=False).order_by("?").first()
    else:
        film = (Challenge.objects.get(
            pk=filter_choice.split("_")[1]).films.order_by("?").first().film)
    template_name = "user/index.html"
    context = {
        "form": RandomForm(initial={"filter_choice": filter_choice}),
        "page": "random",
        "film": film,
    }
    return render(request, template_name, context)
