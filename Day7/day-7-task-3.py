import random
import hangman_art
import hangman_word_list

chosen_word = random.choice(hangman_word_list.word_list)
print(hangman_art.logo)
print("The word has been chosen")
print(f'Pssst, the solution is {chosen_word}.')
lives = 6
print(f"You have {lives} lives left")

display = []
for letters in chosen_word:
    display.append("_")
print(display)
tried_letters = []

while "_" in display:
    if lives > 0:
        counter = 0
        guess = input("Guess a letter: ").lower()
        if guess not in tried_letters:
            tried_letters += guess
            if guess in chosen_word:
                for letter in chosen_word:  
                    if letter == guess:
                        display[counter] = guess
                    counter += 1
                print("Thats right")
                pending_letters = display.count("_")
                if pending_letters > 0:
                    print(f"Just {pending_letters} more letters to guess")
                    print(display)
                else:
                    print("You Won")
                    print(f"The word was {chosen_word}")
            else:
                lives -= 1
                print("Nope, You guessed wrong")
                print(f"You have {lives} more lives left")
                print(hangman_art.stages[lives])
        else:
            print("You've already tried this letter")
    elif lives == 0:
        print("You lose")
        break


  
    



