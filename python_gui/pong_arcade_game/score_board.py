import turtle


class ScoreBoard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.player_score = 0
        self.color("white")
