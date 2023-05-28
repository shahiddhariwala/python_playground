from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(-20, 270)
        self.display_score()

    def increase_score(self):
        self.score += 1
        self.display_score()

    def write_to_board(self, text):
        self.clear()
        self.write(text, False, "center", ("fira-sans", 18, "normal"))

    def display_score(self):
        score_string = f"Score is: {self.score}"
        self.write_to_board(text=score_string)

    def display_game_over(self):
        self.goto(0, 0)
        self.write_to_board(f"Game over!\nYour score is {self.score}")
