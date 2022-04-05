import art
import random
import game_data
import os

def get_random_data():
   return game_data.data[random.randint(0,len(game_data.data)-1)]

def compare(A,B):
   if A["follower_count"] > B["follower_count"]:
      return A
   elif B["follower_count"] > A["follower_count"]:
      return B

def higherorlower():
   score = 0
   is_user_wrong = False
   while not is_user_wrong:
      if score == 0:
         print(art.logo)
      if score == 0:
         A = get_random_data()
         B = get_random_data()
      else: 
         A = B
         B = get_random_data()
      print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}")
      print(art.vs)
      print(f"Compare B: {B['name']}, a {B['description']}, from {B['country']}")
      higher = compare(A,B)
      guess = input("Who has more followers? Type 'A' or 'B':")
      if guess == "A":
         guess = A
      elif guess == "B":
         guess = B
      os.system('clear')
      print(art.logo)
      if guess == higher:
         score += 1
         print(f"You're right! Current score: {score}.")
      else:
         print(f"Sorry, that's wrong. Final score: {score}.")
         is_user_wrong = True
         
higherorlower()