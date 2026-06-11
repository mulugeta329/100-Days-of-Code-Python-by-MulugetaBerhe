import os

def clear_terminal():
    """Clears the terminal screen across different operating systems."""
    os.system('cls' if os.name == 'nt' else 'clear')

# --- BASIC MATHEMATICAL OPERATIONS (OUTPUT FUNCTIONS) ---

def add(n1, n2):
    """Returns the sum of two numerical values."""
    return n1 + n2

def subtract(n1, n2):
    """Returns the difference of two numerical values."""
    return n1 - n2

def multiply(n1, n2):
    """Returns the product of two numerical values."""
    return n1 * n2

def divide(n1, n2):
    """Returns the quotient of two numerical values. Prevents zero-division faults."""
    if n2 == 0:
        return "ERROR: Division by zero is undefined."
    return n1 / n2

# Mapping operations to a structural dictionary for quick access
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    """Executes a continuous arithmetic calculation loop utilizing return values."""
    print("==================================================")
    print("     ENTERPRISE MATH & CALCULATIONS ENGINE       ")
    print("==================================================")
    
    # Defensive Input for the first number
    try:
        num1 = float(input("Enter first numerical coefficient: "))
    except ValueError:
        print("❌ Invalid input. Coefficient must be a number.")
        return calculator() # Restart fresh if input is invalid

    accumulating = True

    while accumulating:
        # Display available mathematical symbols
        for symbol in operations:
            print(f" [ {symbol} ] ")
            
        operation_symbol = input("Select an operational math symbol: ").strip()
        
        if operation_symbol not in operations:
            print("❌ Invalid operational operator. Try again.")
            continue

        # Defensive Input for the second number
        try:
            num2 = float(input("Enter next numerical coefficient: "))
        except ValueError:
            print("❌ Invalid input. Coefficient must be a number.")
            continue

        # Fetch the function from our operations dictionary and execute it
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print("\n--------------------------------------------------")
        print(f"📊 Result: {num1} {operation_symbol} {num2} = {answer}")
        print("--------------------------------------------------\n")

        # Handle errors gracefully before offering continuity options
        if str(answer).startswith("ERROR"):
            input("Press Enter to clear the terminal and reboot the engine...")
            clear_terminal()
            calculator()
            return

        choice = input(f"Type 'y' to continue calculating with {answer}, 'n' to start fresh, or 'exit' to turn off: ").lower().strip()

        if choice == 'y':
            num1 = answer # The output becomes the new input parameter
        elif choice == 'n':
            accumulating = False
            clear_terminal()
            calculator() # Recursion: The function calls itself to start completely over
        else:
            accumulating = False
            print("\n==================================================")
            print("  System offline. Arithmetic cycles completed.   ")
            print("==================================================")

# Initialize the program
calculator()