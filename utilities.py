"""
"""
from io import BytesIO

from django.core.files import File
from PIL import Image


def compress_image(image):
    im = Image.open(image)
    rgb_im = im.convert("RGB")
    im_io = BytesIO()
    rgb_im.save(im_io, "JPEG", optimize=True, quality=70)
    name = image.name.split("/")[-1]
    new_image = File(im_io, name=name)
    return new_image
