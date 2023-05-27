import turtle
from random_color import get_random_color
import random as r

directions = [0, 90, 180, 270, 360]

inny = turtle.Turtle()
inny.pensize(12)
inny.speed("fastest")
for _ in range(200):
    inny.color(get_random_color())
    inny.forward(30)
    inny.setheading(r.choice(directions))

screen = turtle.Screen()
screen.exitonclick()
