import turtle
import random

turtle.colormode(255)
color_list = [(199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (222, 224, 227), (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155), (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203), (150, 115, 120), (202, 185, 190), (40, 72, 82), (46, 73, 62)]

def random_color():
    rgb = random.choice(color_list)
    return rgb


def square(rows, columns):
    start_x, start_y = -250, -250
    for row in range(rows):
        for column in range(columns):
            x = start_x + column * 50
            y = start_y + row * 50
            turtle.teleport(x, y)
            turtle.dot(20, random_color())



turtle.ht()
square(10, 10)

screen = turtle.Screen()
screen.exitonclick()