import art
import os
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
	return cards[random.randint(0,len(cards)-1)]

def calculate_score(cardlist):
	if len(cardlist) == 2 and sum(cardlist) == 21:
		return 0
	if 11 in cardlist and sum(cardlist) > 21:
		cardlist[cardlist.index(11)] = 1
	return sum(cardlist)

def final_score_printer(your_score, dealer_score):
	if your_score > 21 and dealer_score > 21:
		return "You went over. You lose"
	if your_score == dealer_score:
		return "Draw!"
	elif dealer_score == 0:
		return "You Lose!, Opponent has Blackjack"
	elif your_score == 0:
		return "You Win! You have a Blackjack"
	elif your_score > 21:
		return "You went over. You lose"
	elif dealer_score > 21:
		return "Opponent went over. You win"
	elif your_score > dealer_score:
		return "You win!"
	else:
		return "You lose!"

def blackjack():
	print(art.logo)
	your_cards = []
	dealers_cards = []
	game_end = False
	for deal in range(2):
	    your_cards.append(deal_card())
	    dealers_cards.append(deal_card())
	while not game_end:
	    your_score = calculate_score(your_cards)
	    dealer_score = calculate_score(dealers_cards)
	    print(f"Your cards: {your_cards}, current score: {your_score}")
	    print(f"Computer's first card: {dealers_cards[0]}")

	    if your_score == 0 or dealer_score == 0 or your_score > 21:
	      game_end = True
	    else:
	      user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
	      if user_should_deal == "y":
	        your_cards.append(deal_card())
	      else:
	        game_end = True
	while dealer_score != 0 and dealer_score < 17:
	    dealers_cards.append(deal_card())
	    dealer_score = calculate_score(dealers_cards)

	print(f"Your final hand: {your_cards}, final score: {your_score}")
	print(f"Computer's final hand: {dealers_cards}, final score: {dealer_score}")
	print(final_score_printer(your_score, dealer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  os.system('clear')
  blackjack()
