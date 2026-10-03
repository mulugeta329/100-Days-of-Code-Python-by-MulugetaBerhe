def reset(self):
        """Clears existing segment turtles from screen and respawns baseline body."""
        for seg in self.segments:
            seg.goto(1000, 1000) # Move off-screen
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]