MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 300,
    "coffee": 300,
}

profit = {
    "revenue": 0
}


def report():
    for res in resources:
        print(str(res) + ": " + str(resources[res]))
    print("Profit: " + str(profit["revenue"]))


def checkResources(coffee):
    for ingredient, amount in MENU[coffee]["ingredients"].items():
        if resources[ingredient] < amount:
            print("Sorry is not enough " + str(ingredient))
            return False
    return True


def coinInsert(coffee):
    print("Please Insert Coins")
    quarters = int(input("quarters:"))
    dimes = int(input("dimes:"))
    nickels = int(input("nickels:"))
    pennies = int(input("pennies:"))

    val = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)

    if val < MENU[coffee]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return None
    else:
        change = val - MENU[coffee]["cost"]
        profit["revenue"] += (val - change)
        print("Here is " + str(change) + " dollars in change.")
        makeCoffee(coffee)
        print("Here is your " + str(coffee))


def makeCoffee(coffee):
    for typ, amount in resources.items():
        resources[typ] -= MENU[coffee]["ingredients"][typ]


# Intro command
coffeeOn = True
while coffeeOn:
    coffee = input("What would you like? (espresso/latte/cappuccino):")
    if coffee == "off":
        coffeeOn = False
    if coffee == "report":
        report()
    else:
        if checkResources(coffee):
            coinInsert(coffee)
