import turtle as t
from shape_challenges import random_rgb_colour

def draw_spirograph():
    t.colormode(255)
    turtle = t.Turtle()
    turtle.speed("fastest")

    for _ in range(72):
        turtle.pencolor(random_rgb_colour())
        turtle.circle(100)
        turtle.left(5.0)

    screen = t.Screen()
    screen.exitonclick()