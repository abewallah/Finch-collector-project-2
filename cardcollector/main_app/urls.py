from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('decks/', views.decks_index, name='decks_index'),
    path('decks/add_deck/', views.add_deck, name='add_deck'),
    path('decks/<int:deck_id>/', views.decks_detail, name='decks_detail'),

    path('decks/<int:deck_id>/add_card/<int:card_id>/', views.add_card, name='add_card'),
    path('decks/<int:deck_id>/remove_card/<int:card_id>/', views.remove_card, name='remove_card'),
    
    path('decks/<int:deck_id>/add_rating/', views.add_rating, name='add_rating'),
   
    path('decks/<int:deck_id>/update_deck/', views.update_deck, name="update_deck"),
    path('decks/<int:deck_id>/delete_deck/', views.delete_deck, name='delete_deck'),


    path('accounts/signup/', views.signup, name='signup')

]