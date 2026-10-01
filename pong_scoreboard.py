from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 60, "bold")

class Scoreboard(Turtle):
    """Renders real-time score updates for left and right active player channels."""
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """Refreshes canvas overlay with current game score totals."""
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)

    def l_point(self):
        """Increments left player score balance."""
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        """Increments right player score balance."""
        self.r_score += 1
        self.update_scoreboard()