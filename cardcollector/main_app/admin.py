from django.contrib import admin
from .models import Card, Rating, Deck

# Register your models here.
admin.site.register(Deck)
admin.site.register(Card)
admin.site.register(Rating)
