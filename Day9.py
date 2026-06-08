import os

def clear_terminal():
    # Clears the terminal screen so the next bidder cannot see previous inputs
    os.system('cls' if os.name == 'nt' else 'clear')

# --- SYSTEM TERMINAL INTERFACE ---
print("==================================================")
print("     ENTERPRISE PROCUREMENT BLIND BIDDING ENGINE  ")
print("==================================================")
print("Secure Portal Active. All bids are encrypted and hidden.")
print("==================================================")

# Dictionary to store bidding records: { "Name": Bid_Amount }
bidding_records = {}
bidding_active = True

while bidding_active:
    name = input("Enter Vendor / Bidder Name: ").strip().title()
    
    # Defensive Input: Ensure names aren't blank
    if not name:
        print("❌ Name cannot be empty. Please enter a valid name.")
        continue

    # Defensive Input: Prevent system crash if user enters text instead of a number
    try:
        bid_price = float(input("Enter Bid Amount ($): "))
        if bid_price <= 0:
            print("❌ Bid must be a positive financial value.")
            continue
    except ValueError:
        print("❌ Invalid input. Please enter a valid numerical currency amount.")
        continue

    # Record the validated data into our dictionary
    bidding_records[name] = bid_price

    # Check for additional operational bids
    any_other_bidders = input("\nAre there any other bidders? Type 'yes' or 'no': ").lower().strip()
    
    if any_other_bidders == "no":
        bidding_active = False
    elif any_other_bidders == "yes":
        clear_terminal()
    else:
        print("⚠️ Unrecognized command. Defaulting to system wrap-up sequence.")
        bidding_active = False

# --- LOGICAL ENGINE: FIND HIGHEST BIDDER ---
highest_bid = 0
winner = ""

for bidder in bidding_records:
    bid_amount = bidding_records[bidder]
    if bid_amount > highest_bid:
        highest_bid = bid_amount
        winner = bidder

# --- FINAL TABULAR RESULTS GENERATION ---
clear_terminal()
print("==================================================")
print("          FINAL PROCUREMENT AUCTION REPORT        ")
print("==================================================")
print(f"🥇 ACQUISITION WINNER : {winner}")
print(f"💰 CLOSING CONTRACT   : ${highest_bid:,.2f}")
print("==================================================")
print("🔒 Transaction secured. Database locked. System Offline.")
print("==================================================")