"""
"""
from django.shortcuts import render
from challenges.models import Challenge

def challenge_list(request):
    """
    """
    challenges = Challenge.objects.all()
    template_name = "index.html"
    context = {
        "page": "chlist",
        "challenges": challenges,
    }
    return render(request, template_name, context)

