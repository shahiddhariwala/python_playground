from turtle import Screen
import time
from snake import Snake
from food import Food
from score_board import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("🐍 Snake game 🐍")
screen.bgcolor("black")

# below code stops update on screen, with this turned off we have to manually update screen
screen.tracer(0)
snake = Snake()
food = Food()
score = ScoreBoard()
screen.update()

screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True


def is_game_over():
    snake_head = snake.head
    if snake_head.xcor() >= 285 or snake_head.ycor() >= 285 or snake_head.xcor() <= -285 or snake_head.ycor() <= -285:
        score.display_game_over()
        print("Game over!")
        return True
    return False


while not is_game_over():
    time.sleep(.1)
    screen.update()
    snake.move()
    if snake.head.distance(food) < 15:
        score.increase_score()
        snake.eat_food()
        food.refresh()

screen.exitonclick()
