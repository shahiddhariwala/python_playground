from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.title("Ping Pong Game!")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

player_l = Paddle((-350, 0))
player_r = Paddle((350, 0))
screen.update()
screen.listen()
screen.onkey(player_r.go_up, "Up")
screen.onkey(player_r.go_down, "Down")
screen.onkey(player_l.go_up, "w")
screen.onkey(player_l.go_down, "s")

screen.exitonclick()
