from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    """Models the player entity, handling movement logic and finish-line detection."""
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("forest green")
        self.penup()
        self.go_to_start()
        self.setheading(90)

    def go_up(self):
        """Advances the player forward along the vertical y-axis."""
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        """Resets the player object back to baseline starting coordinates."""
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        """Evaluates whether the player has passed the upper boundary finish line."""
        return self.ycor() > FINISH_LINE_Y