import random
from turtle import Turtle


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.speed("fastest")
        self.color("orange")
        self.refresh()

    def refresh(self):
        x_cord = random.randint(-270, 270)
        y_cord = random.randint(-270, 270)
        self.setpos(x_cord, y_cord)
