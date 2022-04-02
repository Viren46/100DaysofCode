from art import logo
import os
print(logo)

bidders = {}
bidding = True

while bidding is True:
	name = input("Enter your Name:")
	bid = float(input("Enter your Bid Amount:"))
	bidders[name] = bid
	bidding_status = input("Is there anyone else that want's to bid? Type 'yes' or 'no'")
	if bidding_status == 'yes':
		os.system('clear')
	else:
		bidding = False
		max_amount = 0
		bid_winner = ""
		for bid in bidders:
			if bidders[bid] > max_amount:
				bid_winner = bid
				max_amount = bidders[bid]
		print(f"The winner of the bid is {bid_winner} with a amount of Rs{max_amount}")





