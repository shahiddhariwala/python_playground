from turtle import Turtle, Screen
from random_color import get_random_rgb_color

inny = Turtle()
screen = Screen()
screen.title("Spirograph!🥰")

# Important if we want to use rgb rather than named color
screen.colormode(255)
inny.speed("fastest")

for angle in range(0, 360, 5):
    inny.width(3)
    inny.color(get_random_rgb_color())
    inny.circle(150, 360)
    inny.setheading(angle)

screen.exitonclick()
