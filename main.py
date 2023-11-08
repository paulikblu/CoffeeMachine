from Menu import MENU, resources

working = True

def report(water, milk, coffee, money):
    print(f"""water:{water}
milk:{milk}
coffee:{coffee}
money:{money}$""")

def checking_resources(drink_type):
    try:
        if MENU[drink_type]["ingredients"]["water"] > resources["water"]:
            print("Sorry there is not enough water")
        if MENU[drink_type]["ingredients"]["milk"] > resources["milk"]:
            print("Sorry there is not enough milk")
        if MENU[drink_type]["ingredients"]["coffee"] > resources["coffee"]:
            print("Sorry there is not enough coffee")
        else:
            return True
    except KeyError:
        print("sorry, invalid drink")

def coins():
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

def transaction(sum, drink_type):
    if sum < MENU[drink_type]["cost"]:
        print("Sorry, not enough money")
    elif sum > MENU[drink_type]["cost"]:
        change = sum - MENU[drink_type]["cost"]
        rounded_change = round(change, 2)
        cost = MENU[drink_type]["cost"]
        print(f"Here is ${rounded_change} in change")
        print("processing order")
    else:
        cost = sum
        print("processing order")
    return cost

b = 0
b += transaction(4.3, "latte")
print(b)

# while working:
#     water = resources["water"]
#     milk = resources["milk"]
#     coffee = resources["coffee"]
#     money = 0
#     order = input("What would you like? (espresso/latte/cappuccino): ")
#     if order == "off":
#         working = False
#     elif order == "report":
#         report(water, milk, coffee, money)
#     else:
#         checking_resources(order)
#         if checking_resources(order):
#             coins = sum()
#             transaction(coins, order)
#             money += transaction(coins, order)

