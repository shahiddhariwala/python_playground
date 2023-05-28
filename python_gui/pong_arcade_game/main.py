from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.title("Ping Pong Game!")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

player_1 = Paddle(1)
player_2 = Paddle(2)
screen.update()
screen.listen()
screen.onkey(player_1.go_up, "Up")
screen.onkey(player_1.go_down, "Down")
screen.onkey(player_2.go_up, "w")
screen.onkey(player_2.go_down, "s")

screen.exitonclick()
