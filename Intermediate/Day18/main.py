from turtle import Turtle, Screen
import random

def drawSquare(turtle, distance):
    for _ in range(0, 4):
        turtle.forward(float(distance))
        turtle.right(float(90))

def drawDashedLine(turtle, line_distance, dash_length):
    distance_moved = 0
    while distance_moved <= line_distance:
        turtle.forward(float(dash_length))
        turtle.penup()
        turtle.forward(5.0)
        turtle.pendown()
        distance_moved += (float(dash_length) + 5.0)

def drawManySides(turtle):
    colours = ["cornflower blue", "deep pink", "brown", "olive drab", "moccasin", "dark salmon"]
    for sides in range(3, 11):
        total_rotation = 0
        turtle.pencolor(random.choice(colours))
        while total_rotation < 360:
            turtle.forward(100.0)
            angle = 360 / sides
            turtle.right(angle=angle)
            total_rotation += angle

turtle = Turtle()
turtle.shape("turtle")


#drawSquare(turtle=turtle, distance=50.0)
#drawDashedLine(turtle, line_distance=200, dash_length=15)
#drawManySides(turtle)

screen = Screen()
screen.exitonclick()
