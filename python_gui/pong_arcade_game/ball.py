import turtle

MOVEMENT = 10


class Ball(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.setheading(45)
        self.penup()
        self.x_move = MOVEMENT
        self.y_move = MOVEMENT

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounce_y(self):
        """
        Reverses direction in Y axis
        """
        self.y_move *= -1

    def bounce_x(self):
        """
        Reverses direction in X axis
        """
        self.x_move *= -1

    def reset_position(self):
        self.bounce_x()
        self.goto(0, 0)
