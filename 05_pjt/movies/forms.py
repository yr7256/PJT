
from platform import release
from django import forms
from .models import Movie


class MovieForm(forms.ModelForm):
    genre_a = 'comedy'
    genre_b = 'horror'
    genre_c = 'romance'
    genre_choice = [(genre_a, '코미디'), (genre_b, '공포'), (genre_c, '로맨스')]
    genre = forms.ChoiceField(choices=genre_choice)
    score = forms.FloatField(max_value=5.0, min_value=0.5,
                             widget=forms.NumberInput(attrs={'step': "0.5"}))
    # release_date = forms.DateField(
    #     widget=forms.DateInput(
    #         format=('%Y-%m-%d'),
    #         attrs={'class': 'form-control', 'placeholder': 'Select a date', 'type': 'date'}
    #     )
    # )

    class Meta:
        model = Movie
        fields = '__all__'
        widgets = {
            'release_date': forms.DateInput(format=('%Y-%m-%d'), attrs={'class': 'form-control', 'placeholder': 'Select a date', 'type': 'date'}),
        }
