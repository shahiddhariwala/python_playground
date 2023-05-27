from turtle import Turtle, Screen

inny = Turtle()
screen = Screen()
screen.title("Etch-a-Sketch")

movement = 10


def move_forward():
    inny.forward(movement)


def move_backward():
    inny.backward(movement)


def rotate_clockwise():
    inny.right(movement)


def rotate_counter_clockwise():
    inny.left(movement)


def clear_screen():
    inny.clear()
    inny.penup()
    inny.home()
    inny.pendown()


screen.listen()

screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=rotate_counter_clockwise)
screen.onkey(key="d", fun=rotate_clockwise)
screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()
