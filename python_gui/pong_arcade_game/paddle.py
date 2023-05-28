import turtle

MOVEMENT = 20


class Paddle(turtle.Turtle):
    def __init__(self, player_number=1):
        super().__init__()
        self.player_number = player_number
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        if player_number == 1:
            self.x_pos = 350
        else:
            self.x_pos = -350
        self.goto(self.x_pos, 0)

    def update_screen(self):
        screen = self.screen
        screen.update()

    def go_up(self):
        y_pos = self.ycor()
        if y_pos < 260:
            self.goto(self.x_pos, y_pos + MOVEMENT)
            self.update_screen()

    def go_down(self):
        y_pos = self.ycor()
        if y_pos > -260:
            self.goto(self.x_pos, y_pos - MOVEMENT)
            self.update_screen()
