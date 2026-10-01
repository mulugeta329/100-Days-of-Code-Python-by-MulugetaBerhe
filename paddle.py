from turtle import Turtle

UP_BOUND = 250
DOWN_BOUND = -250
MOVE_STEP = 20

class Paddle(Turtle):
    """Models a responsive user paddle entity on the graphics canvas."""
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        # Default turtle shape is 20x20. Stretching length by 5 creates a 100x20 vertical paddle
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        """Moves paddle up along the vertical axis if within top bounds."""
        if self.ycor() < UP_BOUND:
            new_y = self.ycor() + MOVE_STEP
            self.goto(self.xcor(), new_y)

    def go_down(self):
        """Moves paddle down along the vertical axis if within bottom bounds."""
        if self.ycor() > DOWN_BOUND:
            new_y = self.ycor() - MOVE_STEP
            self.goto(self.xcor(), new_y)