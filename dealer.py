from deck import CardDeck


class Dealer:

  def __init__(self):
    self.card_deck = CardDeck()

  def calculate_total(self, hand):
    total = sum([self.card_value(card['rank']) for card in hand]) % 10
    return total

  def card_value(self, rank):
    if rank.isdigit():
      return int(rank)
    elif rank in ['10', 'J', 'Q', 'K']:
      return 0
    else:  # 'A'
      return 1

  def draw_hand(self, num_cards):
    hand = [self.card_deck.draw_card() for _ in range(num_cards)]
    return hand

  def play_baccarat(self):
    #print('Playing')
    player_hand = self.draw_hand(2)
    banker_hand = self.draw_hand(2)
    
    player_total = self.calculate_total(player_hand)
    banker_total = self.calculate_total(banker_hand)

    print (f'player draws a hand {player_hand}')
    print (f'banker draws a hand {banker_hand}')
    print (f'{player_total} vs {banker_total}')
    
    if player_total == 8 or player_total == 9 or banker_total == 8 or banker_total == 9:
      temp ='player' if player_total > banker_total else 'banker' if banker_total > player_total else 'tie'
      print (f'player {player_total} vs banker {banker_total}, {temp} wins')
      return temp

    if player_total <= 5:
      player_hand.append(self.card_deck.draw_card())
      player_total = self.calculate_total(player_hand)
      print (f'player draws a card, {player_hand[2]}, new total is {player_total}')
      
    if player_total < 8:
      if banker_total <= 5:
        banker_hand.append(self.card_deck.draw_card())
        banker_total = self.calculate_total(banker_hand)
        print (f'banker draws a card, {banker_hand[2]}, new total is {banker_total}')

    # Determine the winner
    if player_total > banker_total:
      return 'player'
    elif banker_total > player_total:
      return 'banker'
    else:
      return 'tie'
