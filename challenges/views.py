"""
"""
from django.shortcuts import render

from challenges.models import Challenge


def challenge_list(request):
    """
    """
    challenges = Challenge.objects.all()
    template_name = "user/cinema/chlist.html"
    context = {
        "challenges": challenges,
    }
    return render(request, template_name, context)
