from turtle import Turtle

# --- STRUCTURAL ENGINE CONSTANTS ---
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    """Manages the creation, movement vectoring, and orientation parameters of the snake body."""
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Spawns initial structural snake body segment entities at baseline coordinates."""
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        """Chains segment positions chronologically so trailing pieces step into the spot ahead."""
        # Loop backwards through the segment array list: (Start, Stop, Step)
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
            
        # Command the leading master head object to drive forward
        self.head.forward(MOVE_DISTANCE)

    # --- DIRECTIONAL CONTROLS WITH DEFENSIVE REVERSE BLOCKING ---
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)