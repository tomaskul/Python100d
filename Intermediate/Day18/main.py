import turtle as t
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
        angle = 360 / sides
        turtle.pencolor(random.choice(colours))
        for _ in range(sides):
            turtle.forward(100.0)
            turtle.right(angle)

def randomRgbColour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


def drawRandomWalk(turtle, step_count):
    #colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepPink", "LightSeaGreen", "olive drab", "moccasin", "dark salmon"]
    turns = [0.0, 90.0, 180.0, 270.0]

    turtle.hideturtle()
    turtle.pen(pensize=15)
    turtle.speed(8)

    for _ in range(step_count):
        turtle.pencolor(randomRgbColour())
        turn_angle = random.choice(turns)
        turtle.setheading(turn_angle)
        turtle.forward(25)


turtle = t.Turtle()
t.colormode(255)
#turtle.shape("turtle")


#drawSquare(turtle=turtle, distance=50.0)
#drawDashedLine(turtle, line_distance=200, dash_length=15)
#drawManySides(turtle)
drawRandomWalk(turtle, 200)


screen = t.Screen()
screen.exitonclick()
