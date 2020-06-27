"""
"""
from bestmoments.models import BestImage
from bestmoments.models import WebmVideo
from django.shortcuts import render


def best_image_list(request):
    """
    """
    images = BestImage.objects.order_by("image")
    template_name = "user/index.html"
    context = {"page": "bmoments", "images": images}
    return render(request, template_name, context)

def webms(request):
    """
    """
    webms = WebmVideo.objects.all()
    template_name = "user/webms.html"
    context = {"webms": webms }
    return render(request, template_name, context)
