import random
from turtle import Turtle, Screen

rainbow_colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
is_race_on = False
screen = Screen()
screen.title("Turtle Race")
screen.setup(width=500, height=500)
user_bet = screen.textinput("Make a bet", "Choose a color(from rainbow) of turtle who will win?")

turtles_list = []
start_x_pos = -230
start_y_pos = -180

for color in rainbow_colors:
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(color)
    new_turtle.goto(x=start_x_pos, y=start_y_pos)
    start_y_pos += 50
    turtles_list.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles_list:
        if turtle.xcor() > 230:
            is_race_on = False
            winner_turtle_color = turtle.pencolor()
            if user_bet == winner_turtle_color:
                print(f"You have won!, Winner turtle is {winner_turtle_color}")
            else:
                print(f"You have lost!, Winner turtle is {winner_turtle_color}")
        turtle.forward(random.randint(5, 10))

screen.exitonclick()
