"""
"""
import json
from datetime import date

from challenges.models import FilmChallenge
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from filmlist.forms import RandomForm
from filmlist.models import Episode
from filmlist.models import Film
from filmlist.models import Season


def add_new_episodes(episodes, season):
    """
    """
    for episode in episodes:
        del episode["id"]
        episode["season"] = season
        duration = episode["duration"]
        if not duration:
            del episode["duration"]
        print(episode)
        Episode.objects.create(**episode).save()


def add_new_seasons(seasons, film):
    """
    """
    for season in seasons:
        episodes = season["episodes"]
        new_season = Season.objects.create(number=int(season["number"]),
                                           film=film)
        new_season.save()
        add_new_episodes(episodes, season)


@login_required(login_url="/login?next=/admin/cinema/filmlist/")
def admin_film_list(request):
    """
    """
    if request.method == "DELETE":
        film_id = int(json.loads(request.body)["film_id"])
        Film.objects.get(pk=film_id).delete()
        return HttpResponse(status=200)
    if request.method == "POST":
        film_json = json.loads(request.body)["film"]
        pk = film_json["id"]
        seasons = film_json["seasons"]
        del film_json["id"]
        del film_json["seasons"]
        db_film = None if not pk else Film.objects.filter(pk=pk).first()
        db_film_f = Film.objects.filter(
            title=film_json["title"],
            year=film_json["year"],
            director=film_json["director"],
        ).first()
        db_film_f = db_film_f if db_film_f else None
        # update
        if db_film:
            for key, val in film_json.items():
                setattr(db_film, key, val)
            db_film.save()
            serial = db_film.serial
            if serial:
                new_seasons = list(
                    filter(
                        None,
                        [
                            new_season if new_season["id"] == "" else None
                            for new_season in seasons
                        ],
                    ))
                update_seasons = list(
                    filter(
                        None,
                        [
                            new_season if new_season["id"] != "" else None
                            for new_season in seasons
                        ],
                    ))
                for season, episodes in serial:
                    new_season_info = None
                    for new_season in update_seasons:
                        if int(new_season["id"]) == season.id:
                            new_season_info = new_season
                    if not new_season_info:
                        season.delete()
                    else:
                        season.number = int(new_season_info["number"])
                        season.save()
                        new_episodes = list(
                            filter(
                                None,
                                [
                                    new_episode
                                    if new_episode["id"] == "" else None for
                                    new_episode in new_season_info["episodes"]
                                ],
                            ))
                        update_episodes = list(
                            filter(
                                None,
                                [
                                    new_episode
                                    if new_episode["id"] != "" else None for
                                    new_episode in new_season_info["episodes"]
                                ],
                            ))
                        for episode in episodes:
                            new_episode_info = None
                            for new_episode in update_episodes:
                                if int(new_episode["id"]) == episode.id:
                                    new_episode_info = new_episode
                            if not new_episode_info:
                                episode.delete()
                            else:
                                episode.number = int(new_episode_info["number"])
                                if new_episode_info["duration"]:
                                    episode.duration = int(new_episode_info["duration"])
                                episode.title = new_episode_info["title"]
                                episode.is_watched = new_episode_info["is_watched"]
                                episode.save()
                        add_new_episodes(new_episodes, season)
                if not (new_seasons or update_seasons):
                    db_film.is_movie = True
                    db_film.save()
                elif new_seasons:
                    add_new_seasons(new_seasons, db_film)
            elif seasons:
                add_new_seasons(seasons, db_film)
            return HttpResponse(status=200)
        # create if does not exist
        elif not db_film_f:
            new_film = Film.objects.create(**film_json)
            new_film.save()
            add_new_seasons(seasons, new_film)
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=400)
    if request.method == "GET":
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
        film = (FilmChallenge.objects.filter(
            challenge__id=filter_choice.split("_")[1],
            is_done=False).order_by("?").first())
    template_name = "user/cinema/random.html"
    context = {
        "film": film,
        "form": RandomForm(initial={"filter_choice": filter_choice}),
    }
    return render(request, template_name, context)
