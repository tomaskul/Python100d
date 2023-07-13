from turtle import Turtle, Screen

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

turtle = Turtle()
turtle.shape("turtle")



#drawSquare(turtle=turtle, distance=50.0)
#drawDashedLine(turtle, line_distance=200, dash_length=15)

screen = Screen()
screen.exitonclick()
