print("Welcome to the tip calculator!")
bill = float(input("What was the total bill?"))
tip_percentage = float(input("How much tip would you like to give?"))
people_count = int(input("How many people to split the bill?"))
per_person_amount = round((bill/people_count * (1 + tip_percentage / 100)),2)
print(f"Each person should pay: Rs{per_person_amount}")