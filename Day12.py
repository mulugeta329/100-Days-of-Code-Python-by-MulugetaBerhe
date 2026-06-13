import random

# --- GLOBAL CONSTANTS (Scope Definition Practice) ---
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def set_difficulty():
    """Sets game difficulty by returning matching global turn constants."""
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower().strip()
    if level == "easy":
        return EASY_LEVEL_TURNS
    elif level == "hard":
        return HARD_LEVEL_TURNS
    else:
        print("⚠️ Unrecognized choice. Defaulting system to HARD difficulty.")
        return HARD_LEVEL_TURNS

def check_answer(guess, answer, turns):
    """Compares the user guess against the target answer. Returns updated remaining turns."""
    if guess > answer:
        print("📈 Too high.")
        return turns - 1
    elif guess < answer:
        print("📉 Too low.")
        return turns - 1
    else:
        print(f"🎯 CORRECT! You found the hidden coordinate: {answer}")
        return 0

def game():
    """Executes the core loop control sequence for the Guessing Engine."""
    print("==================================================")
    print("        ADVANCED NUMERICAL MATCH ENGINE v1.0      ")
    print("==================================================")
    print("System initializing... Guessing a integer vector between 1 and 100.")
    
    # Generate the secret target number
    answer = random.randint(1, 100)
    
    # Set the tracking variable using global bounds
    turns = set_difficulty()
    
    guess = 0
    # Keep running until the guess matches the answer or turns hit 0
    while guess != answer and turns > 0:
        print(f"\n⚡ Security attempts remaining: {turns}")
        
        # Defensive Input Catching: Avoid program crash if input isn't a valid integer
        try:
            guess = int(input("Make a guess: "))
        except ValueError:
            print("❌ Invalid entry! Please input a valid numerical integer.")
            continue
            
        # Process performance checks and decrement lives if wrong
        turns = check_answer(guess, answer, turns)
        
        if turns == 0 and guess != answer:
            print("\n💀 OUT OF ATTEMPTS. Execution cycle terminated.")
            print(f"🔒 The correct hidden target was: {answer}")

    print("==================================================")

# Execute the application runtime
game()