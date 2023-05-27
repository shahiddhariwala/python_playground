from turtle import Turtle, Screen
import random as r

inny = Turtle()
screen = Screen()
side = 3
colors = ["red", "yellow", "purple", "green", "violet", "orange", "pink", "wheat", "gray"]


def draw_polygon(num_sides):
    inny.color(r.choice(colors))
    angle = 360 / side
    for _ in range(num_sides):
        inny.forward(100)
        inny.right(angle)


for num_sides in range(3, 11):
    draw_polygon(num_sides)
    side += 1

screen.exitonclick()
