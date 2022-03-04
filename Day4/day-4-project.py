import random
import sys

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

# Rock wins against scissors.
# Scissors win against paper.
# Paper wins against rock.

choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. ")
if choice == '1':
    choice = paper
elif choice == '0':
    choice = rock
elif choice == '2':
    choice = scissors
else:
    print("Your selection in invalid")
    quit()

computer_choice = str(random.randint(0,2))
if computer_choice == '1':
    computer_choice = paper
    if choice == paper:
        print(f"You chose \n{choice}")
        print(f"Computer chose \n{computer_choice}")
        print("Try again!")
    elif choice == scissors:
        print(f"You chose \n{choice}")
        print(f"Computer chose \n{computer_choice}")
        print("You win")
    else:
        print(f"You chose \n{choice}")
        print(f"Computer chose \n{computer_choice}")
        print("You lose")
elif computer_choice == '0':
    computer_choice = rock
    if choice == rock:
        print(f"You chose \n{choice}")
        print(f"Computer chose \n{computer_choice}")
        print("Try again!")
    elif choice == paper:
        print(f"You chose \n{choice}")
        print(f"Computer chose \n{computer_choice}")
        print("You win")
    else:
        print(f"You chose \n{choice}")
        print(f"Computer chose \n{computer_choice}")
        print("You lose")
elif computer_choice == '2':
    computer_choice = scissors
    if choice == scissors:
        print(f"You chose \n{choice}")
        print(f"Computer chose \n{computer_choice}")
        print("Try again!")
    elif choice == rock:
        print(f"You chose \n{choice}")
        print(f"Computer chose \n{computer_choice}")
        print("You win")
    else:
        print(f"You chose \n{choice}")
        print(f"Computer chose \n{computer_choice}")
        print("You lose")




