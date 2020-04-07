"""
"""
from challenges.models import Challenge
from django.shortcuts import render


def challenge_list(request):
    """
    """
    challenges = Challenge.objects.all()
    template_name = "user/index.html"
    context = {
        "page": "chlist",
        "challenges": challenges,
    }
    return render(request, template_name, context)
