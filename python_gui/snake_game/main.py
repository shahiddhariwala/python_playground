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

screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True


def is_game_over():
    snake_head = snake.head
    if snake_head.xcor() >= 300 or snake_head.ycor() >= 300:
        print("Game over")
        return True
    return False


while not is_game_over():
    time.sleep(.1)
    screen.update()
    snake.move()

screen.exitonclick()
