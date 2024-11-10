from dealer import Dealer
from player import Player

#insert player strategies here
p1 = Player(1, ['player', 'banker', 'player', 'player', 'banker', 'banker'])
p2 = Player(2, ['banker', 'player', 'banker', 'banker', 'player', 'player'])
totalG = 0
d1 = Dealer()
d2 = Dealer()


def eval_bet(pBet, pAm, gRes):  #(win/lose/tie, bet_amount1/2,game_result)
  isBank = (gRes == 'banker')
  temp1 = ''  #did I win
  temp2 = 0  #how much?
  if gRes == 'tie':
    temp1 = 'tie'
    temp2 = pAm
  elif pBet != gRes:  #lose
    temp1 = 'lose'
    temp2 = 0
  else:  #win
    temp1 = 'win'
    temp2 = pAm * 2
  if isBank and gRes != 'tie':
    temp2 *= .95
    #if temp2 != 0:
    #print(f"*beep* Banker Fee collected!")
  #game_result to know if I get back commision
  return temp1, temp2


#while p1.current_bankroll > 0 and p2.current_bankroll > 0 and p1.current_bankroll < 9600 and p2.current_bankroll < 9600:
for _ in range(10):
  bet_choice1, bet_amount1 = p1.place_bet()
  bet_choice2, bet_amount2 = p2.place_bet()

  game_result1 = d1.play_baccarat()
  game_result2 = d2.play_baccarat()
  print(f"P1 stats: {eval_bet(bet_choice1, bet_amount1, game_result1)}")
  print(f"P2 stats: {eval_bet(bet_choice2, bet_amount2, game_result2)}")
  #print(f"Game result: {game_result}")
  t1, t2 = eval_bet(bet_choice1, bet_amount1, game_result1)
  t3, t4 = eval_bet(bet_choice2, bet_amount2, game_result2)
  p1.update_bankroll(t1, t2)
  p2.update_bankroll(t3, t4)
  totalG += 1
  print("~~~~~~~~~~")
print(f"Total Games: {totalG}")
print(
    f"P1 Final Bankroll: {p1.current_bankroll} {p1.bust_count} {p1.bet_unit}")
print(
    f"P2 Final Bankroll: {p2.current_bankroll} {p2.bust_count} {p2.bet_unit}")
