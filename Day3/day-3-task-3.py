# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if (float(year) % 4) == 0:
	if (float(year) % 100) == 0:
		if (float(year) % 400) == 0:
			print("Leap year.")
		else:
			print("Not leap year.")
	else:
		print("Leap year.")
else:
	print("Not leap year.")



