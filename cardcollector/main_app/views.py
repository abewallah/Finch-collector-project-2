from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Card, Rating, Deck
from .forms import RatingForm, CardForm, DeckForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
    return render(request, 'home.html')



def about(request):
    return render(request, 'about.html')



def decks_index(request):
    if request.method == 'POST':
        deck_form = DeckForm(request.POST)
        if deck_form.is_valid():
            new_deck = deck_form.save(commit=False)
            new_deck.user = request.user
            new_deck.save()
            return redirect('decks_index')

    decks = Deck.objects.filter(user=request.user)
    deck_form = DeckForm()
    context = { 'decks_data': decks, 'deck_form': deck_form}
    return render(request, 'decks/index.html', context)


@login_required
def add_deck(request):
    deck_form = DeckForm()
    deck = DeckForm(request.POST)

    context = {
        'deck_form': deck_form
    }

    if deck.is_valid():
        new_deck = deck.save()
        return redirect('decks_detail', deck_id = new_deck.id)
    
    return render(request, 'decks/new.html', context)




def decks_detail(request, deck_id):
    deck = Deck.objects.get(id=deck_id)
    cards_in_deck = Card.objects.exclude(id__in = deck.cards.all().values_list('id'))
    rating_form = RatingForm()
    context = { 
        'deck': deck, 
        'rating_form': rating_form,
        'cards': cards_in_deck
        }
    return render(request, 'decks/detail.html', context)



@login_required
def update_deck(request, deck_id):
    deck = Deck.objects.get(id=deck_id)

    if request.method == 'GET':
        deck_form = DeckForm(instance = deck)

        context = {
            'deck': deck,
            'deck_form': deck_form
        }
        return render(request, 'decks/edit.html', context)
    else:
        deck_form = DeckForm(request.POST, instance = deck)
        if deck_form.is_valid():
            deck_form.save()
        return redirect('decks_detail', deck_id= deck_id)


@login_required
def add_card(request, deck_id, card_id):
    Deck.objects.get(id=deck_id).cards.add(card_id)

    return redirect('decks_detail', deck_id=deck_id)


@login_required
def remove_card(request, deck_id, card_id):
    
    deck = Deck.objects.get(id=deck_id)
    card = Card.objects.get(id=card_id)
    deck.cards.remove(card)

    return redirect('decks_detail', deck_id=deck_id)




@login_required
def add_rating(request, deck_id):
    form = RatingForm(request.POST)

    if form.is_valid():
        new_rating = form.save(commit=False)
        new_rating.deck_id = deck_id
        new_rating.save()

    return redirect('decks_detail', deck_id=deck_id)



@login_required
def delete_deck(request, deck_id):
    if request.method == 'POST':
        Deck.objects.get(id=deck_id).delete()

    return redirect('decks_index')


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid:
            user = form.save()
            login(request, user)

            return redirect('decks_index')
        else:
            error_message = 'Invalid Credentials - Try again.'

    form = UserCreationForm()
    context = { 'form' : form }  

    return render(request, 'registration/signup.html', context)

