import os

def clear_terminal():
    """Clears the console screen across platform environments."""
    os.system('cls' if os.name == 'nt' else 'clear')


# =====================================================================
# 📦 EXTERNAL MODULE SIMULATION (Angela Yu's Course Blueprint Classes)
# =====================================================================

class MenuItem:
    """Models each individual drink item on the menu."""
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }

class Menu:
    """Models the menu containing all available drink items."""
    def __init__(self):
        self.menu = [
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.50),
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.50),
            MenuItem(name="cappuccino", water=250, milk=100, coffee=24, cost=3.00),
        ]

    def get_items(self):
        """Returns all the names of the available menu items as a formatted string."""
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options.strip("/")

    def find_drink(self, order_name):
        """Searches the menu for a specific drink by name. Returns a MenuItem object if it exists."""
        for item in self.menu:
            if item.name == order_name:
                return item
        print("❌ System Fault: That item is not available within our distribution array.")
        return None

class CoffeeMaker:
    """Models the mechanical hardware that manages inventory and brews the beverages."""
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self):
        """Prints a detailed diagnostics status report of all raw material stock capacities."""
        print(f" 💧 Water Capacity  : {self.resources['water']}ml")
        print(f" 🥛 Milk Capacity   : {self.resources['milk']}ml")
        print(f" 🫘 Coffee Capacity : {self.resources['coffee']}g")

    def is_resource_sufficient(self, drink):
        """Returns True when an item's ingredients can be fulfilled, False if resources are low."""
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"❌ System Fault: Insufficient underlying capacity for [{item.upper()}].")
                can_make = False
        return can_make

    def make_coffee(self, order):
        """Deducts the required ingredients from the inventory resources and dispenses beverage."""
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"☕ Optimization Complete: Asset [{order.name.upper()}] successfully dispensed. Enjoy!")

class MoneyMachine:
    """Models the financial currency transaction gateway processing ledger."""
    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickels": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        self.profit = 0.0
        self.money_received = 0.0

    def report(self):
        """Prints the total accumulated corporate profit holding balances."""
        print(f" 💰 Total Capital   : ${self.profit:,.2f}")

    def process_coins(self):
        """Prompts user for coin quantities and returns the calculated currency value sum."""
        print("🪙 Financial Transaction Gateway Active. Please insert currency denominations:")
        for coin in self.COIN_VALUES:
            try:
                self.money_received += int(input(f"  How many {coin}?: ")) * self.COIN_VALUES[coin]
            except ValueError:
                print(f"⚠️ Unrecognized currency token. Appending $0.00 for {coin}.")
        return self.money_received

    def make_payment(self, cost):
        """Returns True if payment accepted, or False if currency amount is lacking."""
        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            if change > 0:
                print(f"💵 Dispensing transaction change balance: ${change:,.2f}")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("❌ Transaction Refused: Insufficient fiscal credit assets submitted. Refunding currency...")
            self.money_received = 0
            return False


# =====================================================================
# 🎮 CORE OBJECT-ORIENTED APP RUNTIME ENGINE
# =====================================================================
def run_oop_matrix():
    clear_terminal()
    
    # 💎 OOP INTENT: Constructing instances from our modular Class Blueprints
    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()
    
    is_operational = True

    while is_operational:
        print("==================================================")
        print("      OBJECT-ORIENTED DISPENSING MATRIX v2.0      ")
        print("==================================================")
        # Dynamically fetch operational choice vectors straight from our menu object methods
        options = menu.get_items()
        print(f" Available Coordinates: [ {options.replace('/', ' | ').title()} ]")
        print("--------------------------------------------------")
        
        user_choice = input("Select operational service vector (or type 'report'/'off'): ").lower().strip()

        if user_choice == "off":
            is_operational = False
            print("\nShutting down matrix interface. OOP Diagnostic connection closed.")
        elif user_choice == "report":
            print("\n=========================================")
            print("      SYSTEM DIAGNOSTIC METRICS REPORT   ")
            print("=========================================")
            coffee_maker.report()
            money_machine.report()
            print("=========================================\n")
        else:
            # Query the menu object to find if the drink entity exists
            drink = menu.find_drink(user_choice)
            
            if drink is not None:
                # Target Verification Gate 1: Check hardware capacity via coffee_maker object method
                if coffee_maker.is_resource_sufficient(drink):
                    # Target Verification Gate 2: Handle currency checkout transaction via money_machine object method
                    if money_machine.make_payment(drink.cost):
                        # Action: command hardware object to execute process and deduct inventory logs
                        coffee_maker.make_coffee(drink)
                        
        if is_operational:
            input("\nPress Enter to return to the Main Control Sequence...")
            clear_terminal()

if __name__ == "__main__":
    run_oop_matrix()