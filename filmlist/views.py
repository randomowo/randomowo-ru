"""
"""
from datetime import date

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from challenges.models import FilmChallenge
from filmlist.forms import RandomForm
from filmlist.models import Film
from filmlist.models import Episode
from filmlist.models import Season

@login_required(login_url="/login?next=/admin/cinema/filmlist/")
def admin_film_list(request):
    """
    """
    if request.method == "POST":
        print(request.POST)

    films = Film.objects.order_by("is_watched")
    watched = films.filter(is_watched=True).count()
    template_name = "admin/cinema/flist.html"
    context = {
        "films": films,
        "films_watched": watched,
        "films_count": films.count(),
        "next_year": date.today().year + 1,
    }
    return render(request, template_name, context)

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
        film = FilmChallenge.objects.filter(challenge__id=filter_choice.split("_")[1], is_done=False).order_by("?").first()
    template_name = "user/cinema/random.html"
    context = {
        "film": film,
        "form": RandomForm(initial={"filter_choice": filter_choice}),
    }
    return render(request, template_name, context)
