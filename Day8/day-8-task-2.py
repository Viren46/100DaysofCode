#Write your code below this line ๐
def prime_checker(number):
	if number == 1 or number == 0:
		print("It's not a prime number.")
	elif number == 2:
		print("It's a prime number.")
	else:
		for numbers in range(2,number):
			if number % numbers == 0:
				print("It's not a prime number.")
				break
		else:
			print("It's a prime number.")






#Write your code above this line ๐
    
#Do NOT change any of the code below๐
n = int(input("Check this number: "))
prime_checker(number=n)