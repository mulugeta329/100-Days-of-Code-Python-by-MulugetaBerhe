import turtle as t
import random
import os

def clear_terminal():
    """Clears the console screen across platform environments."""
    os.system('cls' if os.name == 'nt' else 'clear')

# --- SYSTEM INITIALIZATION & WINDOW CONFIGURATION ---
screen = t.Screen()
# Establish the width and height of our graphical display window
screen.setup(width=500, height=400)

clear_terminal()
print("==================================================")
print("     ALGORITHMIC RACING SIMULATOR ENGINE v1.0     ")
print("==================================================")

# Prompt the user for a predictive guess using a GUI text box popup
user_bet = screen.textinput(
    title="Make Your Wager", 
    prompt="Predict the winning vector color: (red/orange/yellow/green/blue/purple)"
).lower().strip()

# Core tracking states
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []
is_race_on = False

# 💎 OBJECT INSTANTIATION: Constructing multiple distinct object instances
for turtle_index in range(0, 6):
    new_turtle = t.Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    
    # Position each turtle along the starting grid on the left edge of the screen
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    
    # Store the individual instantiated object into our tracking array matrix
    all_turtles.append(new_turtle)

# Safe Execution Gate: Only start the calculation loop if the user placed a valid wager
if user_bet in colors:
    is_race_on = True
    print(f"Prediction Logged: User has wagered capital on asset [{user_bet.upper()}].")
    print("Simulation starting... Computing velocity vectors...")
else:
    print("⚠️ Warning: Invalid or missing color wager token. Simulation running in headless mode.")
    is_race_on = True

# --- CORE SIMULATION MOTOR LOOP ---
while is_race_on:
    for turtle in all_turtles:
        # Check boundary condition: standard turtle graphics width center is 0 (coordinates are -250 to +250)
        # A turtle coordinate x exceeding 230 means its front edge has passed the 250 finish line mark
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            
            print("\n=========================================")
            print("            RACE ANALYSIS REPORT         ")
            print("=========================================")
            print(f"🥇 WINNING VECTOR: {winning_color.upper()}")
            print("-----------------------------------------")
            
            if winning_color == user_bet:
                print(f"🏆 SUCCESS: Your prediction was accurate! [{winning_color.upper()}] completed the cycle first.")
            else:
                print(f"📉 LOSS: Your prediction failed. [{winning_color.upper()}] took the matrix milestone.")
            print("=========================================\n")
            
        # Generate random forward movement steps to simulate variable velocity
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

# Keep the graphic window open on screen until clicked
screen.exitonclick()