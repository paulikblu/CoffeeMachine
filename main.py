from Menu import MENU, resources

working = True

def report(water, milk, coffee, money):
    print(f"""water:{water}ml
milk:{milk}ml
coffee:{coffee}g
money:{money}$""")

def checking_resources(drink_type, water, coffee, milk):
    try:
        if MENU[drink_type]["ingredients"]["water"] > water:
            print("Sorry there is not enough water")
        if MENU[drink_type]["ingredients"]["coffee"] > coffee:
            print("Sorry there is not enough coffee")
        if drink_type != "espresso" and MENU[drink_type]["ingredients"]["milk"] > milk:
            print("Sorry there is not enough milk")
        else:
            return True
    except KeyError:
        print("sorry, invalid drink")

def coins():
    try:
        quarter = 0.25
        dime = 0.10
        nickle = 0.05
        penny = 0.01
        quarters = quarter * float(input("Insert the number of quarters: "))
        dimes = dime * float(input("Insert the number of dimes: "))
        nickles = nickle * float(input("Insert the number of nickles: "))
        pennies = penny * float(input("Insert the number of pennies: "))
        sum = quarters + dimes + nickles + pennies
        return sum
    except ValueError:
        print("Invalid number")
        return 0


water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]
money = 0

while working:
    order = input("What would you like? (espresso/latte/cappuccino): ")
    if order == "off":
        working = False
    elif order == "report":
        report(water, milk, coffee, money)
    else:
        if checking_resources(order, water, coffee, milk):
            sum = coins()
            if sum < MENU[order]["cost"]:
                print("Sorry, not enough money")
            else:
                change = sum - MENU[order]["cost"]
                if change > 0:
                    rounded_change = round(change, 2)
                    money += MENU[order]["cost"]
                    print(f"Here is ${rounded_change} in change")
                else:
                    money += sum
                water -= MENU[order]["ingredients"]["water"]
                coffee -= MENU[order]["ingredients"]["coffee"]
                if order != "espresso":
                    milk -= MENU[order]["ingredients"]["milk"]
                print(f"Here is your {order}. Enjoy!")
