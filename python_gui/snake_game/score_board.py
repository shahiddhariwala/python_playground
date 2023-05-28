from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(-20, 280)
        self.display_score()

    def update_score(self):
        self.score += 1
        self.display_score()

    def display_score(self):
        self.clear()
        score_string = f"Score is: {self.score}"
        self.write(score_string, False, "center", ("fira-sans", 10, "normal"))
