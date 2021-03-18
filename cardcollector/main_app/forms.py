from django import forms
from .models import Rating, Card, Deck


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['date', 'grade']

class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ['name', 'attributes', 'types','description', 'atk', 'defense']

class DeckForm(forms.ModelForm):
    class Meta:
        model = Deck
        fields = ['name','description']

