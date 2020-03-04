"""
"""
from django.contrib import admin
from challenges.models import Challenge

class ChallengeAdmin(admin.ModelAdmin):
    list_display = ["task"]


admin.site.register(Challenge, ChallengeAdmin)
