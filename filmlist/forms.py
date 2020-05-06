"""
"""
from challenges.models import Challenge
from challenges.models import FilmChallenge
from django import forms
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

    challenge_is_done = forms.BooleanField(required=False, )

    def __init__(self, *args, **kwargs):
        super(FilmAdminForm, self).__init__(*args, **kwargs)
        film = self.instance
        film_challenge = FilmChallenge.objects.filter(film=film).first()
        if film_challenge:
            self.initial["challenge_is_done"] = film_challenge.is_done
        else:
            self.initial["challenge_is_done"] = None
        if film.title:
            series = Series.objects.filter(film=film).first()
            self.initial["episodes"] = series.episodes if series else None

    def clean_title(self):
        """
        """
        title = self.cleaned_data.get("title", None)
        year = self.data.get("year", None)
        film = Film.objects.filter(title=title).first()
        print(self.changed_data)
        if film and film.year == int(year) and "title" in self.changed_data:
            raise forms.ValidationError("Film already exist")
        else:
            return title

    def clean_episodes(self):
        """
        """
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
        episodes = self.cleaned_data.get("episodes", None)
        film = super(FilmAdminForm, self).save(commit=commit)
        film.save()
        if not film.is_movie and episodes is not None:
            series = Series.objects.filter(film=film).first()
            if series:
                series.episodes = episodes
                series.save()
            else:
                Series.objects.create(film=film, episodes=episodes)
        if film.is_challenge:
            challange = FilmChallenge.objects.get(film=film)
            challenge_is_done = self.cleaned_data.get("challenge_is_done",
                                                      False)
            challange.is_done = challenge_is_done
            challange.save()
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


class RandomForm(forms.Form):
    """
    """

    OPTIONS = [
        ("all", "all"),
        ("watched", "watched"),
        ("unwatched", "unwatched"),
    ]
    for ch in Challenge.objects.all():
        OPTIONS.append((f"ch_{ch.id}", ch.task))

    filter_choice = forms.ChoiceField(required=False,
                                      choices=OPTIONS,
                                      label="",
                                      initial="unwatched")
