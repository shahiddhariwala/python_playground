from turtle import Turtle


def get_part():
    part = Turtle("square")
    part.penup()
    part.color("white")
    return part


class Snake:
    snake_body = []

    def __init__(self):
        self.initialise_snake_body()

    def move(self):
        for part_num in range(len(self.snake_body) - 1, 0, -1):
            new_x_cord = self.snake_body[part_num - 1].xcor()
            new_y_cord = self.snake_body[part_num - 1].ycor()
            self.snake_body[part_num].goto(new_x_cord, new_y_cord)

        self.snake_body[0].forward(20)

    def initialise_snake_body(self):
        x_cord = 0
        for _ in range(3):
            part = get_part()
            part.goto(x_cord, 0)
            x_cord -= 20
            self.snake_body.append(part)
