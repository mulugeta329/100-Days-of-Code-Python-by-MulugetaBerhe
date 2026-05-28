print("Automated Customs & Shipping calculator")
weight = float(input("What is the package weight in kg:\n"))
cost = 0

if weight > 30:
    print("Package exceeds maximum weight limit. Shipping denied.")
else:
    # Fix 1: Added .lower() to country to make it bulletproof
    country = input("What is your destination country? ").lower()
    is_restricted = input("Does the package contain restricted items? Type 'yes' or 'no': ").lower()
    
    if country == "uk" and is_restricted == "yes":
        print("Shipping denied: Restricted items cannot be shipped to the UK.")
    else:
        if weight <= 5:
            cost += 15.00
        elif weight <= 15:
            cost += 35.00
        else:
            cost += 60.00
            
        express_delivery = input("Do you want Express delivery? Type 'yes' or 'no':\n").lower()
        if express_delivery == 'yes':
            cost += 20.00
            express_fee = 20.00
        else:
            express_fee = 0.00
            
        # Professional Output Summary
        print("\n--- Shipping Summary ---")
        print(f"Total Due: ${cost:.2f}")