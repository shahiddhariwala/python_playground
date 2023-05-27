from turtle import Turtle, Screen
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.title("🐍 Snake game 🐍")
screen.bgcolor("black")

# below code stops update on screen, with this turned of we have to manually update screen
screen.tracer(0)
snake = Snake()
screen.update()

is_game_on = True

while is_game_on:
    time.sleep(.5)
    screen.update()
    snake.move()

screen.exitonclick()
