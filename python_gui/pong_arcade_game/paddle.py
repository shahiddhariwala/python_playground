import turtle

MOVEMENT = 20


class Paddle(turtle.Turtle):
    def __init__(self, initial_pos):
        super().__init__()
        self.initial_pos = initial_pos
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(initial_pos)

    def update_screen(self):
        screen = self.screen
        screen.update()

    def go_up(self):
        y_pos = self.ycor()
        if y_pos < 260:
            self.goto(self.xcor(), y_pos + MOVEMENT)
            self.update_screen()

    def go_down(self):
        y_pos = self.ycor()
        if y_pos > -260:
            self.goto(self.xcor(), y_pos - MOVEMENT)
            self.update_screen()
