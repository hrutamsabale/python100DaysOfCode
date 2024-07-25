MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0
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
    "milk": 200,
    "coffee": 100,
}

coins = {
    "Penny":0.01,
    "Nickel":0.05,
    "Dime":0.1,
    "Quarter":0.25
}
current_resources = resources
while True:
    coffee_wanted = input("What coffee would you like? 'Espresso', 'Latte' or 'Cappuccino' : ").lower()
    if coffee_wanted=="report":
        print(f"The are the current resources: ")
        for key in current_resources:
            print(f"{key} : {current_resources[key]}")
        print("\n")
        continue
    if coffee_wanted not in MENU:
        print("No such coffee available!\n")
        continue
    not_available=[]
    water_required = MENU[coffee_wanted]["ingredients"]["water"]
    water_available = current_resources["water"]
    coffee_required = MENU[coffee_wanted]["ingredients"]["coffee"]
    coffee_available = current_resources["coffee"]
    milk_required = MENU[coffee_wanted]["ingredients"]["milk"]
    milk_available = current_resources["milk"]
    cost_of_coffee = MENU[coffee_wanted]["cost"]
    if water_available<water_required:
        not_available.append("Water")
    if coffee_available<coffee_required:
        not_available.append("Coffee")
    if milk_available<milk_required:
        not_available.append("Milk")
    if len(not_available)!=0:
        print("Sorry! We're out of: ")
        for item in not_available:
            print(item)
        print("\n")
        continue
    print(f"The {coffee_wanted} costs: ${cost_of_coffee} Please enter the coins:")
    pennies = int(input("Pennies: "))
    nickels = int(input("Nickels: "))
    dimes = int(input("Dimes: "))
    quarters = int(input("Quarters: "))
    total_money_entered = (pennies*0.01) + (nickels*0.05) + (dimes*0.1) + (quarters*0.25)
    if total_money_entered<cost_of_coffee:
        print("That's not enough money. Here's you refund.\n")
        continue
    money_to_be_returned = total_money_entered - cost_of_coffee
    print(f"Here's your change ${money_to_be_returned}\n")
    print(f"And here's your {coffee_wanted.capitalize()}: ☕\nEnjoy\n")
    current_resources["water"] = water_available - water_required
    current_resources["coffee"] = coffee_available - coffee_required
    current_resources["milk"] = milk_available - milk_required
