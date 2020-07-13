"""
"""
from django.shortcuts import render

from challenges.models import Challenge
from challenges.models import FilmChallenge


def challenge_list(request):
    """
    """
    challenge_list = Challenge.objects.all()
    challenges = []
    for ch in challenge_list:
        challenges.append((ch, FilmChallenge.objects.filter(challenge=ch).order_by("position")))
    template_name = "user/cinema/chlist.html"
    context = {
        "challenges" : challenges,
    }
    return render(request, template_name, context)
