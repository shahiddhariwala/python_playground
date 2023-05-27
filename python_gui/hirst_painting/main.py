# import colorgram
# extracted_colors = colorgram.extract("Hirstspotpainting.jpg", 30)
# rgb_colors = []
# for col in extracted_colors:
#     rgb_colors.append((col.rgb.r, col.rgb.g, col.rgb.r))
from turtle import Turtle, Screen
from random import choice

rgb_colors = [(144, 76, 144), (188, 165, 188), (166, 153, 166), (14, 46, 14), (139, 185, 139),
              (146, 56, 146), (42, 110, 42), (59, 120, 59), (145, 170, 145), (87, 35, 87), (64, 152, 64),
              (220, 209, 220), (110, 37, 110), (100, 145, 100), (165, 99, 165), (91, 122, 91), (158, 138, 158),
              (177, 104, 177), (55, 52, 55), (206, 182, 206), (68, 48, 68), (73, 51, 73), (173, 201, 173),
              (175, 198, 175), (213, 182, 213), (37, 47, 37)]

inny = Turtle()
screen = Screen()
screen.colormode(255)
screen.title("Hirst Painting!")
x_cord = 0
y_cord = 0
inny.penup()
inny.hideturtle()
num_of_dot_per_side = 6
inny.setpos(x_cord, y_cord)


def draw_dot():
    inny.dot(25, choice(rgb_colors))


for num in range(1, (num_of_dot_per_side ** 2) + 1):
    draw_dot()
    x_cord += 50
    if num % num_of_dot_per_side == 0:
        y_cord += 50
        x_cord = 0
    inny.setpos(x_cord, y_cord)

screen.exitonclick()
