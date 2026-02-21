# assignment2-carddraw.py
# Using an API that simulates dealing cards from a deck, this program will deal out (print) 5 cards.
# Author: Zoe McNamara Harlowe

import requests

url = "https://deckofcardsapi.com/"
response = requests.get(url)

# Shuffle a new deck
shuffle_url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
shuffle_response = requests.get(shuffle_url)
deck_data = shuffle_response.json()
deck_id = deck_data['deck_id']

# Draw 5 cards from the deck
draw_url = "https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=5"
draw_response = requests.get(draw_url.format(deck_id=deck_id))
cards_data = draw_response.json()
cards = cards_data['cards']

# Print the drawn cards in format "No. of Suit"
for card in cards:
    print(f"{card['value']} of {card['suit']}")

# Congratulate the user for pair, three of a kind, straight and all the same suit
suits = [card['suit'] for card in cards]
values = [card['value'] for card in cards]
suit_counts = {suit: suits.count(suit) for suit in set(suits)}
value_counts = {value: values.count(value) for value in set(values)}

# All the same suit
if 5 in suit_counts.values():
    print("All cards are of the same suit! Congratulations!")

# Pair - 2 of the same value and suit
if 2 in value_counts.values():
    print("Congratulations! You have drawn a pair!")

# Three of a kind
if 3 in value_counts.values():
    print("Congratulations! You have drawn three of a kind!")

# Straight
value_order = ['ACE', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'JACK', 'QUEEN', 'KING']
value_indices = sorted([value_order.index(value) for value in values])
is_straight = all(value_indices[i] + 1 == value_indices[i + 1] for i in range(len(value_indices) - 1))
if is_straight:
    print("Congratulations! You have drawn a straight!")
