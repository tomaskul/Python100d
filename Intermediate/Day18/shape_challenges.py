import turtle as t
import random

def drawSquare(side_length):
    '''Draws a square of length sides.'''
    turtle = t.Turtle()
    turtle.shape("turtle")
    for _ in range(0, 4):
        turtle.forward(float(side_length))
        turtle.right(float(90))

    screen = t.Screen()
    screen.exitonclick()


def drawDashedLine(line_distance, dash_length):
    '''Draws a dashed line of specified distance and gap lenghts.'''
    turtle = t.Turtle()
    turtle.shape("turtle")

    distance_moved = 0
    while distance_moved <= line_distance:
        turtle.forward(float(dash_length))
        turtle.penup()
        turtle.forward(5.0)
        turtle.pendown()
        distance_moved += (float(dash_length) + 5.0)

    screen = t.Screen()
    screen.exitonclick()


def drawManySides():
    '''Draws shapes from triangle to dekagon, in different colours, on top of one another.'''
    turtle = t.Turtle()
    turtle.shape("turtle")

    colours = ["cornflower blue", "deep pink", "brown", "olive drab", "moccasin", "dark salmon"]
    for sides in range(3, 11):
        angle = 360 / sides
        turtle.pencolor(random.choice(colours))
        for _ in range(sides):
            turtle.forward(100.0)
            turtle.right(float(angle))

    screen = t.Screen()
    screen.exitonclick()


def randomRgbColour():
    '''Returns a tuple of a random rgb colour, i.e., (r, g, b).'''
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


def drawRandomWalk(step_count):
    '''Draws a random walk over specified number of steps.'''
    t.colormode(255)
    turtle = t.Turtle()
    turtle.hideturtle()
    turtle.pen(pensize=15)
    turtle.speed(8)

    turns = [0.0, 90.0, 180.0, 270.0]

    for _ in range(step_count):
        turtle.pencolor(randomRgbColour())
        turn_angle = random.choice(turns)
        turtle.setheading(turn_angle)
        turtle.forward(25)
    
    screen = t.Screen()
    screen.exitonclick()


#drawSquare(distance=50.0)
#drawDashedLine(line_distance=200, dash_length=15)
#drawManySides()
#drawRandomWalk(200)