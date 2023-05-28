from turtle import Turtle

MOVE_DISTANCE = 20
def get_part():
    part = Turtle("square")
    part.penup()
    part.color("white")
    return part


DIRECTIONS = {
    "left": 180,
    "right": 0,
    "up": 90,
    "down": 270
}

class Snake:

    def __init__(self):
        self.snake_body = []
        self.initialise_snake_body()
        self.head = self.snake_body[0]
        self.head.color("red")
        self.head.shape("circle")

    def move(self):
        for part_num in range(len(self.snake_body) - 1, 0, -1):
            new_x_cord = self.snake_body[part_num - 1].xcor()
            new_y_cord = self.snake_body[part_num - 1].ycor()
            self.snake_body[part_num].goto(new_x_cord, new_y_cord)

        self.head.forward(MOVE_DISTANCE)

    def initialise_snake_body(self):
        x_cord = 0
        for _ in range(3):
            part = get_part()
            part.goto(x_cord, 0)
            x_cord -= 20
            self.snake_body.append(part)

    def get_snake_head(self):
        return self.head

    def up(self):
        if self.head.heading() != DIRECTIONS["down"]:
            self.head.setheading(DIRECTIONS["up"])

    def right(self):
        if self.head.heading() != DIRECTIONS["left"]:
            self.head.setheading(DIRECTIONS["right"])

    def down(self):
        if self.head.heading() != DIRECTIONS["up"]:
            self.head.setheading(DIRECTIONS["down"])

    def left(self):
        if self.head.heading() != DIRECTIONS["right"]:
            self.head.setheading(DIRECTIONS["left"])

    def eat_food(self):
        new_part = get_part()
        new_part.goto(self.snake_body[-1].position())
        self.snake_body.append(new_part)
