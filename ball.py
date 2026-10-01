from turtle import Turtle

class Ball(Turtle):
    """Manages spatial trajectory, speed acceleration, and reflection calculations for the ball."""
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        """Calculates trajectory step updates based on active velocity vectors."""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """Inverts the vertical trajectory vector upon colliding with top/bottom walls."""
        self.y_move *= -1

    def bounce_x(self):
        """Inverts the horizontal trajectory vector and accelerates ball speed upon paddle impact."""
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        """Resets ball position to absolute origin, reverses serve direction, and restores baseline speed."""
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()