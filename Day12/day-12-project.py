import art
import random


def restart_game():
	restart = input("Do you want to play again? Type 'yes' or 'no':").lower()
	if restart == 'yes':
		number_guessing_game()
	else:
		return

def number_guessing_game():
	print(art.logo)
	print("Welcome to the Number Guessing Game!")
	print("I'm thinking of a number between 1 and 100.")
	random_number = random.randint(1,100)
	difficulty = input("Choose a difficulty. Type 'easy' or 'hard':").lower()
	if difficulty == 'hard':
		turns = 5
	elif difficulty == 'easy':
		turns = 10
	attempts = 0
	while attempts < turns:
		guess = int(input("Make a guess:"))
		if guess < random_number:
			print("Too low.")
			attempts += 1
			if attempts != turns:
				print("Guess again.")
				print(f"You have {turns-attempts} attempts remaining to guess the number.")
		elif guess == random_number:
			print(f"You got it! The answer was {random_number}.")
			restart_game()
			return
		elif guess > random_number:
			print("Too high.")
			attempts += 1
			if attempts != turns:
				print("Guess again.")
				print(f"You have {turns-attempts} attempts remaining to guess the number.")
	if attempts == turns:
		print("You've run out of guesses, you lose.")
		print(f"The number was {random_number}")
		restart_game()
		

number_guessing_game()