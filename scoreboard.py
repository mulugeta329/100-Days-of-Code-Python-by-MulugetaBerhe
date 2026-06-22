from turtle import Turtle

# --- ALIGNMENT CONSTANTS ---
ALIGNMENT = "center"
FONT = ("Courier", 16, "bold")

class Scoreboard(Turtle):
    """Manages the UI layout overlay layer, text rendering, and tracked scoring states."""
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        """Clears old prints and renders the updated active scoring matrix values."""
        self.clear()
        self.write(f"AMPLIFIED SCORE INDEX: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """Increments the internal tracking balance counter and refreshes UI."""
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        """Fires a terminal game-over text banner in the absolute center coordinate workspace."""
        self.goto(0, 0)
        self.write("🚨 PIPELINE CRASH: GAME OVER", align=ALIGNMENT, font=FONT)