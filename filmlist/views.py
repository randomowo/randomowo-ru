"""
"""
from django.shortcuts import render

from challenges.models import Challenge
from filmlist.forms import RandomForm
from filmlist.models import Film


def film_list(request):
    """
    """
    films = Film.objects.order_by("is_watched")
    watched = films.filter(is_watched=True).count()
    template_name = "user/cinema/flist.html"
    context = {
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
            pk=filter_choice.split("_")[1]).films.order_by("?").filter(
                is_done=False).first().film)
    template_name = "user/cinema/random.html"
    context = {
        "film": film,
        "form": RandomForm(initial={"filter_choice": filter_choice}),
    }
    return render(request, template_name, context)
