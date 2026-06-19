import turtle as t
import random

# --- SYSTEM INITIALIZATION ---
# Set turtle color mode to 255 to accept explicit RGB tuple values
t.colormode(255)
painter = t.Turtle()
painter.speed("fastest")
painter.hideturtle()

# Prevent the turtle cursor from drawing connecting lines between the dots
painter.penup()

# --- DIGITAL CANVAS PALETTE MAPPING ---
# Premium corporate design RGB color tokens list
rgb_colors = [
    (242, 245, 243), (198, 165, 119), (141, 172, 191), 
    (53, 91, 117), (163, 79, 62), (122, 143, 114), 
    (235, 215, 142), (81, 62, 53), (178, 199, 183)
]

# Configure grid mapping layout constants
DOT_COUNT = 100  # Total asset points to render (10x10 Matrix)
GRID_SPACING = 50 # Graphical pixel coordinates distance allocation
STARTING_X = -220
STARTING_Y = -220

# Relocate drawing origin pointer to center the final artwork on screen
painter.setheading(225)
painter.forward(300)
painter.setheading(0)

# --- ALGORITHMIC GRID GENERATION ENGINE ---
print("==================================================")
print("       GENERATIVE ART ENGINE INITIALIZED         ")
print("==================================================")
print("Compiling coordinate spaces... Rendering canvas vector matrix.")

for dot_count in range(1, DOT_COUNT + 1):
    # Select a random color asset from our portfolio tuple matrix
    chosen_color = random.choice(rgb_colors)
    
    # Render an explicit point vector
    painter.dot(20, chosen_color)
    painter.forward(GRID_SPACING)
    
    # Positional Check: If a row of 10 dots is finished, pivot and reset for the next line
    if dot_count % 10 == 0:
        painter.setheading(90)
        painter.forward(GRID_SPACING)
        painter.setheading(180)
        painter.forward(GRID_SPACING * 10)
        painter.setheading(0)

print("🎨 Synthesis Complete: Abstract canvas matrix vector generated.")
print("==================================================")

# Instantiates a UI screen frame entity that stays open until clicked
screen = t.Screen()
screen.exitonclick()