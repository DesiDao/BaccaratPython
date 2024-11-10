import random


class CardDeck:

  def __init__(self):
    self.reset_deck()

  def reset_deck(self):
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

    self.deck = [{
        'rank': rank,
        'suit': suit
    } for _ in range(6) for rank in ranks for suit in suits]

    random.shuffle(self.deck)
    self.next_draw_index = 0

  def draw_card(self):
    if self.next_draw_index >= len(self.deck):
      self.reset_deck()
    drawn_card = self.deck[self.next_draw_index]
    self.next_draw_index += 1

    return drawn_card
