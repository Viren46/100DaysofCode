# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name_one = name1.lower()
name_two = name2.lower()

true_count = name_one.count("t") + name_two.count("t") + name_one.count("r") + name_two.count("r") + name_one.count("u") + name_two.count("u")  + name_one.count("e") + name_two.count("e")
love_count = name_one.count("l") + name_two.count("l") + name_one.count("o") + name_two.count("o") + name_one.count("v") + name_two.count("v")  + name_one.count("e") + name_two.count("e")
love_score = int(str(true_count) + str(love_count))


if love_score < 10 or love_score > 90:
	print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
	print(f"Your score is {love_score}, you are alright together.")
else:
	print(f"Your score is {love_score}.")