from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
screen = Screen()
screen.title("Ping Pong Game!")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

is_game_on = True
player_l = Paddle((-350, 0))
player_r = Paddle((350, 0))
ball = Ball()

screen.listen()
screen.onkey(player_r.go_up, "Up")
screen.onkey(player_r.go_down, "Down")
screen.onkey(player_l.go_up, "w")
screen.onkey(player_l.go_down, "s")

while is_game_on:

    time.sleep(.1)

    ball.move()
    screen.update()

    # Collision with top & bottom wall

    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    # Collision with paddles
    if ball.distance(player_r) <= 50 and ball.xcor() >= 330 or ball.distance(player_l) <= 50 and ball.xcor() <= -330:
        ball.bounce_x()

    # Detect misses
    if ball.xcor() >= 380 or ball.xcor() <= -380:
        ball.reset_ball()

screen.exitonclick()
