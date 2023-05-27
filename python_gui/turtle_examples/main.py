from turtle import Turtle, Screen

inny = Turtle()
inny.shape("turtle")
# Drawing Circle
inny.color("purple")
inny.circle(200, 360)
inny.shape("circle")
inny.color("red")
inny.circle(300, 360)

screen = Screen()
screen.exitonclick()
