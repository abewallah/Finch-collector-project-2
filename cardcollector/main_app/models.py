from django.db import models
from django.contrib.auth.models import User


class Card(models.Model):
    name = models.CharField(max_length=50)
    attributes = models.CharField(max_length=50)
    types = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    atk = models.IntegerField()
    defense = models.IntegerField()
    
    
    def __str__(self):
        return self.name

class Deck(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)

    cards = models.ManyToManyField(Card, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
         return f'{self.name} is {self.description}'


GRADES = (
    ('S', 'S-Class'),
    ('A', 'A-Class'),
    ('B', 'B-Class'),
    ('C', 'C-Class'),
    ('D', 'D-Class'),
)

class Rating(models.Model):
    date = models.DateField()
    grade = models.CharField(max_length=1,
        choices=GRADES,
        default=GRADES[0][0]
    )
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.get_grade_display()} on {self.date}'