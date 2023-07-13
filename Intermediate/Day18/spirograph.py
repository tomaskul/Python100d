import turtle as t
from shape_challenges import randomRgbColour

def drawSpirograph():
    t.colormode(255)
    turtle = t.Turtle()
    turtle.speed("fastest")

    for _ in range(72):
        turtle.pencolor(randomRgbColour())
        turtle.circle(100)
        turtle.left(5.0)

    screen = t.Screen()
    screen.exitonclick()