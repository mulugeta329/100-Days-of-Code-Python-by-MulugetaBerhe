from turtle import Screen
from paddle import Paddle
from ball import Ball
from pong_scoreboard import Scoreboard
import time
import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_terminal()
print("==================================================")
print("     DUAL-PLAYER PONG VECTOR ENGINE INITIALIZED    ")
print("==================================================")

# --- CANVAS DISPLAY SETUP ---
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Vector Arcade Sandbox: Classic Pong Engine")
screen.tracer(0)

# --- OBJECT INSTANTIATIONS ---
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

# --- DUAL-PLAYER CONTROLS ---
screen.listen()
# Right Player Controls
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
# Left Player Controls
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

# --- MAIN ENGINE MOTOR LOOP ---
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # 1. Top and Bottom Wall Bounce Logic
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # 2. Paddle Impact Collision Detection
    # Checks coordinate proximity (within 50px) alongside horizontal boundary thresholds (x > 320 or x < -320)
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # 3. Out-Of-Bounds Detection (Right side miss -> Left scores point)
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # 4. Out-Of-Bounds Detection (Left side miss -> Right scores point)
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()