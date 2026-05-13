print("--- Business Invoice Generator ---")

# 1. Collect inputs and convert them to the correct data types
subtotal = float(input("Enter the service subtotal: $"))
tax_rate = float(input("Enter the tax rate (e.g., 15 for 15%): "))
late_fee = float(input("Enter any additional late fees: $"))

# 2. Perform the business math
tax_amount = subtotal * (tax_rate / 100)
total_invoice = subtotal + tax_amount + late_fee

# 3. Professional Output
print("\n--- Final Invoice Summary ---")
print(f"Subtotal:   ${subtotal:.2f}")
print(f"Tax ({tax_rate}%): ${tax_amount:.2f}")
print(f"Late Fees:  ${late_fee:.2f}")
print("-" * 25)
print(f"TOTAL DUE:  ${total_invoice:.2f}")