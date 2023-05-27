from turtle import Turtle, Screen
from random_color import get_random_color

inny = Turtle()
screen = Screen()
side = 3


def draw_polygon(num_sides):
    inny.color(get_random_color())
    angle = 360 / side
    for _ in range(num_sides):
        inny.forward(100)
        inny.right(angle)


for sides in range(3, 11):
    inny.speed("fast")
    draw_polygon(sides)
    side += 1

screen.exitonclick()
