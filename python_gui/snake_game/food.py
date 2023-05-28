import random
from turtle import Turtle
import random as r

rainbow_colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        x_cord = random.randint(-270, 270)
        y_cord = random.randint(-270, 270)
        self.setpos(x_cord, y_cord)
        self.color(r.choice(rainbow_colors))
