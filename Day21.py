from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_terminal()
print("==================================================")
print("     COMPLETE ARCADE RENDER ENGINE PLATFORM      ")
print("==================================================")
print("System active. Class inheritance matrices online... Enjoy.")

# --- CANVA FRAME LAYOUT SETUP ---
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Vector Arcade Sandbox: Complete Snake Engine")
screen.tracer(0)

# --- OBJECTS MATRIX INITIALIZATION ---
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# --- KEYBOARD EVENT INTERFACE CONTROLS ---
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# --- CORE MOTOR CALCULATIONS RUNTIME ---
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # 🎯 COLLISION ANALYSIS 1: Intersecting with Food Dot
    # Distance method calculates pixel-to-pixel geometric distance between two turtles
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # 🚨 COLLISION ANALYSIS 2: Hitting Outer Wall Boundaries
    # Screen boundaries are -300 to +300. Custom 280 bounds accounts for the snake segment thickness.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # 💥 COLLISION ANALYSIS 3: Hitting Self (Tail Slicing Loop)
    # Using python list slicing [1:] to easily skip checking the head object against itself
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()