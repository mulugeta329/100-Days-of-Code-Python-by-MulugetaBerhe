from turtle import Turtle
import random

class Food(Turtle):
    """Models the target food element. Inherits directly from the native Turtle graphic class."""
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        # Scale the default 20x20 turtle dot down to a 10x10 point shape
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("cyan")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """Relocates the food coordinate randomly within standard boundary coordinates."""
        # Standard screen is 600x600 (boundaries are -300 to +300). 
        # Placing food at steps of 20 ensures alignment with the snake body movement grid.
        random_x = random.randint(-13, 13) * 20
        random_y = random.randint(-13, 13) * 20
        self.goto(random_x, random_y)