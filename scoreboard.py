from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 16, "bold")

class Scoreboard(Turtle):
    """Manages score tracking, high score file persistence, and overlay UI rendering."""
    def __init__(self):
        super().__init__()
        self.score = 0
        # Load high score from persistent storage on startup
        with open("data.txt", mode="r") as data:
            self.high_score = int(data.read())
            
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        """Clears screen overlay and renders current and high scores."""
        self.clear()
        self.write(f"SCORE: {self.score}  HIGH SCORE: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        """Updates high score if exceeded, saves to data.txt, and resets current score."""
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        """Increments active score and refreshes display."""
        self.score += 1
        self.update_scoreboard()