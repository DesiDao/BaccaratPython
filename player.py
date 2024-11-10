import random


class Player:

  def __init__(self, numb=0, bet_order=None):
    self.initial_bankroll = 1600
    self.current_bankroll = self.initial_bankroll
    self.bet_unit = 25
    self.max_bet = 800
    self.bet_order = bet_order if bet_order else []
    self.original_bet_order = self.bet_order.copy()
    self.pnumb = numb
    self.bust_count = 0
    self.hold_bet = False
    self.current_bet_choice = None
    self.current_bet_amount = None

  def reset_bet_order(self):
    self.bet_order = self.original_bet_order.copy()
    self.bet_unit = 25

  def place_bet(self):
    if self.hold_bet:
      self.hold_bet = False
      #print(f"Player {self.pnumb} is re-betting on {self.current_bet_choice} with amount {self.current_bet_amount}")
      return self.current_bet_choice, self.current_bet_amount
    elif not self.bet_order:
      # If no bet order is specified, place a random bet
      bet_choice = random.choice(['player', 'banker'])
    else:

      bet_choice = self.bet_order.pop(0)
      if not self.bet_order:
        self.reset_bet_order()

      bet_amount = min(self.bet_unit, self.max_bet, self.current_bankroll)
      self.current_bankroll -= bet_amount

      self.current_bet_choice = bet_choice
      self.current_bet_amount = bet_amount

      #print(f"Player {self.pnumb} is betting on {bet_choice} with amount {bet_amount}")
      return bet_choice, bet_amount

  def update_bankroll(self, result, payout):
    if result == 'win' and self.current_bet_amount == self.max_bet:
      self.reset_bet_order()
      self.bet_unit = 25
      print(f"P{self.pnumb}: Oh god that was close!")
    elif result == 'lose' and self.current_bet_amount == self.max_bet:
      self.reset_bet_order()
      self.bet_unit = 25
      self.bust_count += 1
      print(f"P{self.pnumb}: BUST!")
    elif result == 'tie' and self.current_bet_amount == self.max_bet:
      self.hold_bet = True
      print(f"P{self.pnumb}: Trying again at the gates of hell!")
    if result == 'win':
      self.current_bankroll += payout
      self.reset_bet_order()
      #print("I win!")
    elif result == 'lose':
      #print("I lose!")
      self.bet_unit *= 2
      pass
    elif result == 'tie':
      #print("Going again!")
      self.hold_bet = True
      self.current_bankroll += payout
