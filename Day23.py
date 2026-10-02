import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from crossing_scoreboard import Scoreboard
import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_terminal()
print("==================================================")
print("     TURTLE CROSSING CAPSTONE ENGINE v1.0         ")
print("==================================================")

# --- CANVAS DISPLAY CONFIGURATION ---
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Vector Arcade Sandbox: Turtle Crossing Capstone")
screen.tracer(0)

# --- INSTANTIATE OBJECT MODULES ---
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# --- EVENT LISTENERS ---
screen.listen()
screen.onkey(player.go_up, "Up")

# --- MAIN REFRESH MOTOR LOOP ---
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Generate traffic and advance car positions
    car_manager.create_car()
    car_manager.move_cars()

    # 1. Collision Detection: Vehicle Proximity Check
    for car in car_manager.all_cars:
        # Distance calculation handles rectangular car dimensions (20x40 pixel bounding area)
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # 2. Level Clear Detection: Upper Boundary Reach
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()