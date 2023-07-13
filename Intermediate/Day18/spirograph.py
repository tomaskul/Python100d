import turtle as t
from shape_challenges import random_rgb_colour

def draw_spirograph(size_of_gap):
    t.colormode(255)
    turtle = t.Turtle()
    turtle.speed("fastest")

    iterations = 360 / size_of_gap

    for _ in range(int(iterations)):
        turtle.pencolor(random_rgb_colour())
        turtle.circle(100)
        turtle.left(float(size_of_gap))

    screen = t.Screen()
    screen.exitonclick()

draw_spirograph(5.0)