import menu

Water = menu.resources["water"]
Milk = menu.resources["milk"]
Coffee = menu.resources["coffee"]
Money =  0

def requirement_checker(requirement):
    if menu.MENU[requirement]["ingredients"]["water"] <= Water and menu.MENU[requirement]["ingredients"]["milk"] <= Milk and menu.MENU[requirement]["ingredients"]["coffee"] <= Coffee:
        return True
    else:
        if menu.MENU[requirement]["ingredients"]["water"] > Water:
            print("Sorry there is not enough water.")
        if menu.MENU[requirement]["ingredients"]["milk"] > Milk:
            print("Sorry there is not enough milk.")
        if menu.MENU[requirement]["ingredients"]["coffee"] <= Coffee:
            print("Sorry there is not enough coffee.")


def amount_checker(a,b,c,d):
    input = (0.25 * a) + (0.1 * b) + (0.05 * c) + (0.01 * d)
    if input < menu.MENU[user_input]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
    else:
        return input




program_status =  "on"
while program_status != 'off':
    user_input = input("What would you like? (espresso/latte/cappuccino):")
    if user_input == 'off':
        program_status = 'off'
    elif user_input == 'report':
        print(f"""        Water = {Water}ml
        Milk = {Milk}ml
        Coffee = {Coffee}g
        Money =  ${Money}""")
    else:
        current_resources = requirement_checker(user_input)
        if current_resources:
            print("Please insert coins.")
            quarters = int(input("how many quarters?:"))
            dimes = int(input("how many dimes?:"))
            nickles = int(input("how many nickles?:"))
            pennies = int(input("how many pennies?:"))
            coin_sum = amount_checker(quarters, dimes, nickles, pennies)
            if coin_sum is not None:
                Money += coin_sum
                if coin_sum != menu.MENU[user_input]["cost"]:
                    print(f'Here is {coin_sum - menu.MENU[user_input]["cost"]} in change.')
                print(f'Here is your {user_input} ☕️. Enjoy!')
                Water -= menu.MENU[user_input]["ingredients"]["water"]
                Milk -= menu.MENU[user_input]["ingredients"]["milk"]
                Coffee -= menu.MENU[user_input]["ingredients"]["coffee"]


