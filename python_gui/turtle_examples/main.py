from turtle import Turtle, Screen

inny = Turtle()
screen = Screen()
screen.title("Inny Playground!")
inny.shape("turtle")
# Drawing Circle
inny.color("purple")
inny.circle(200, 360)
inny.shape("circle")

# Drawing Square
for _ in range(4):
    inny.forward(100)
    inny.right(90)

# Drawing Dashed Lines

for num in range(30):
    if num % 2 == 0:
        inny.penup()
    else:
        inny.pendown()
    inny.forward(10)

screen.exitonclick()
