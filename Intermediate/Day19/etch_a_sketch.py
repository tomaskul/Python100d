import turtle as t

def etch_a_sketch():
    turtle = t.Turtle()

    def forward():
        turtle.forward(10.0)
    
    def backwards():
        turtle.backward(10.0)

    def turn_counter_clockwise():
        turtle.left(5.0)
    
    def turn_clockwise():
        turtle.right(5.0)

    def clear():
        turtle.clear()
        turtle.penup()
        turtle.home()
        turtle.pendown()

    screen = t.Screen()
    screen.listen()
    screen.onkey(fun=clear, key="c")
    screen.onkey(fun=forward, key="w")
    screen.onkey(fun=backwards, key="s")
    screen.onkey(fun=turn_counter_clockwise, key="a")
    screen.onkey(fun=turn_clockwise, key="d")
    screen.exitonclick()


etch_a_sketch()