"""
"""
from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from filmlist.models import Film
from filmlist.models import Series


class FilmAdminForm(forms.ModelForm):
    """
    """

    episodes = forms.IntegerField(
        required=False,
        validators=[MinValueValidator(1)],
    )

    def clean_episodes(self):
        is_movie = self.cleaned_data.get("is_movie", None)
        episodes = self.cleaned_data.get("episodes", None)
        if not is_movie and episodes is None:
            raise forms.ValidationError("Episodes must be 1 or greater")
        elif is_movie and episodes is not None and episodes != 0:
            raise forms.ValidationError("Episodes must be 0 on null")
        else:
            return episodes

    def save(self, commit=True):
        """
        """
        print("=================")
        episodes = self.cleaned_data.get("episodes", None)
        film = super(FilmAdminForm, self).save(commit=commit)
        if not film.is_movie and episodes is not None:
            print("s")
            film.save()
            Series.objects.create(film=film, episodes=episodes)
        film.save()
        return film

    class Meta:
        models = Film


class SeriesAdminForm(forms.ModelForm):
    """
    """
    def __init__(self, *args, **kwargs):
        super(SeriesAdminForm, self).__init__(*args, **kwargs)
        self.fields["film"] = forms.ModelChoiceField(
            queryset=Film.objects.filter(is_movie=False))
