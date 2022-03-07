#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_letters = []
password_symbols = []
password_numbers = []

for characters in range(0,nr_letters):
	password_letters.append(letters[random.randint(0,len(letters)-1)])
for characters in range(0,nr_symbols):
	password_symbols.append(symbols[random.randint(0,len(symbols)-1)])
for characters in range(0,nr_numbers):
	password_numbers.append(numbers[random.randint(0,len(numbers)-1)])

password_characters = password_letters+password_symbols+password_numbers
print(password_characters)
print(len(password_characters))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
passwordeasy = ""
for characters in range(0,len(password_characters)):
	passwordeasy += password_characters[characters]
print(passwordeasy)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

##Using While not For
passwordhard = ""
while len(passwordhard) != len(password_characters):
	passwordhardchar = random.choice(password_characters)
	if passwordhardchar not in passwordhard:
		passwordhard += passwordhardchar
print(passwordhard)


