import turtle

FONT = ("fira-sans", 36, "normal")


class ScoreBoard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 240)
        self.write(f"{self.l_score}", False, "center", FONT)
        self.goto(100, 240)
        self.write(f"{self.r_score}", False, "center", FONT)

    def l_point(self):
        self.l_score += 1
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.update_score()
