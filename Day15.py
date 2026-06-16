import os

# --- GLOBAL ARCHITECTURAL METRICS (State Machine Inclusions) ---
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.50,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.50,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.00,
    }
}

# Core system assets initial values
profit = 0.0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def clear_terminal():
    """Clears the terminal console workspace across active runtime environments."""
    os.system('cls' if os.name == 'nt' else 'clear')

def check_resources_sufficient(order_ingredients):
    """Returns True if the inventory can fulfill the recipe criteria, otherwise False."""
    for item in order_ingredients:
        if order_ingredients[item] > resources.get(item, 0):
            print(f"❌ System Fault: Insufficient underlying storage vector for [{item.upper()}].")
            return False
    return True

def process_coins():
    """Prompts for physical currency values. Evaluates and returns the aggregated cash float."""
    print("🪙 Financial Transaction Gateway Active. Please insert currency denominations:")
    try:
        total = int(input("  How many quarters ($0.25)?: ")) * 0.25
        total += int(input("  How many dimes ($0.10)?: ")) * 0.10
        total += int(input("  How many nickels ($0.05)?: ")) * 0.05
        total += int(input("  How many pennies ($0.01)?: ")) * 0.01
        return total
    except ValueError:
        print("⚠️ Transaction processing exception: Invalid numerical asset token. Defaulting currency weight to $0.00.")
        return 0.0

def make_payment_successful(money_received, drink_cost):
    """Returns True if payment is accepted, or False if currency amount is lacking."""
    global profit
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        if change > 0:
            print(f"💵 Dispensing transaction change balance: ${change:,.2f}")
        profit += drink_cost
        return True
    else:
        print("❌ Transaction Refused: Insufficient fiscal credit assets submitted. Refunding currency...")
        return False

def deduct_inventory_resources(drink_name, order_ingredients):
    """Subtracts the required recipe ingredients from the current system resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"☕ Optimization Complete: Asset [{drink_name.upper()}] successfully dispensed. Enjoy!")

def generate_system_report():
    """Prints a clear summary of the system's current asset capacities."""
    print("\n=========================================")
    print("      SYSTEM DIAGNOSTIC METRICS REPORT   ")
    print("=========================================")
    print(f" 💧 Water Capacity  : {resources['water']}ml")
    print(f" 🥛 Milk Capacity   : {resources['milk']}ml")
    print(f" 🫘 Coffee Capacity : {resources['coffee']}g")
    print(f" 💰 Total Capital   : ${profit:,.2f}")
    print("=========================================\n")

def run_beverage_matrix():
    """Main execution engine loop controlling state management structures."""
    global resources, profit
    is_operational = True

    while is_operational:
        print("==================================================")
        print("    AUTOMATED BEVERAGE DISPENSING MATRIX v1.0     ")
        print("==================================================")
        print(" Available Coordinates: [ Espresso | Latte | Cappuccino ]")
        print("--------------------------------------------------")
        
        user_choice = input("Select operational service vector (or type 'report'/'off'): ").lower().strip()

        if user_choice == "off":
            is_operational = False
            print("\nShutting down matrix interface. Diagnostic connection closed.")
        elif user_choice == "report":
            generate_system_report()
        elif user_choice in MENU:
            drink = MENU[user_choice]
            # Operational Gate 1: Resource Capacity Audit
            if check_resources_sufficient(drink["ingredients"]):
                # Operational Gate 2: Currency Float Validation
                payment = process_coins()
                # Operational Gate 3: Transaction Completion Audit
                if make_payment_successful(payment, drink["cost"]):
                    deduct_inventory_resources(user_choice, drink["ingredients"])
        else:
            print("❌ Input target selection exception: Out of matrix bounds. Verify choice.")
            
        if is_operational:
            input("\nPress Enter to return to the Main Control Sequence...")
            clear_terminal()

if __name__ == "__main__":
    run_beverage_matrix()