from coffee_machine_data import MENU, resources

profit = 0

def coins():
    total = int(input("how many quarters? ")) * 0.25
    total += int(input("how many dimes? ")) * 0.10
    total += int(input("how many nickels? ")) * 0.05
    total += int(input("how many pennies? ")) * 0.01
    return total


def successful_transaction(received_dollars, drink_price):
    if received_dollars >= drink_price:
        change_back = round(received_dollars - drink_price, 2)
        print(f"Your change {change_back}")

        # add profit
        global profit

        profit += drink_price
        return True
    else:
        print("Not enough money, you get a refund")
        return False


def sufficient_ingredients(order_items):
    for item in order_items:
        if order_items[item] > resources[item]:
            print(f"Not enough {item}")
            return False
        return True


def make_coffee(drink, order_items):
    for item in order_items:
        resources[item] -= order_items[item]
    print(f"here is your {drink}")

machine_works = True

while machine_works:
    coffee_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if coffee_choice == "off":
        machine_works = False
    elif coffee_choice == "report":
        print(f"Water: {resources['water']} ml")
        print(f"Milk: {resources['milk']} ml")
        print(f"Coffee: {resources['coffee']} g")
        print(f"Money: ${profit}")
    else:
        drinking = MENU[coffee_choice]
        if sufficient_ingredients(drinking["ingredients"]):
            paying = coins()
            if successful_transaction(paying, drinking['cost']):
                make_coffee(coffee_choice, drinking["ingredients"])



