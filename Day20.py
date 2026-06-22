from turtle import Screen
from snake import Snake
import time
import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_terminal()
print("==================================================")
print("       ARCADE RENDER PLATFORM ENGINE v1.0         ")
print("==================================================")
print("System active. Initializing canvas frames... Control binding hot.")

# --- DISPLAY CANVAS SETUP ---
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Vector Arcade Sandbox: Snake Engine")

# Turn off automatic turtle trace updates so the window animations don't stutter
screen.tracer(0)

# Instantiate the custom blueprint object class from our module file
snake = Snake()

# --- KEYBOARD KEY EVENT LISTENERS ---
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# --- MAIN ARCADE REFRESH TIMING MOTOR ---
game_is_on = True
while game_is_on:
    # Refresh the game screen manually every 0.1 seconds to render clean movement updates
    screen.update()
    time.sleep(0.1)
    
    # Execute the algorithmic movement transformation step
    snake.move()

screen.exitonclick()