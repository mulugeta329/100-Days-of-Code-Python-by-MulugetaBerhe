from turtle import Turtle

FONT = ("Courier", 18, "bold")

class Scoreboard(Turtle):
    """Handles real-time level rendering and terminal state UI overlays."""
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        """Clears and re-renders active stage tracking text."""
        self.clear()
        self.write(f"STAGE LEVEL: {self.level}", align="left", font=FONT)

    def increase_level(self):
        """Increments internal stage counter and refreshes UI."""
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        """Renders crash event notification in the center coordinate space."""
        self.goto(0, 0)
        self.write("💥 IMPACT DETECTED: GAME OVER", align="center", font=FONT)