from turtle import Turtle, Screen

inny = Turtle()
inny.color("red")
inny.shape("turtle")
inny.forward(300)
inny.shapesize(2)
screen = Screen()
screen.exitonclick()
print(screen.canvheight, screen.canvwidth)
