import turtle as t

def etch_a_sketch():
    turtle = t.Turtle()

    def forward(x, y):
        turtle.forward(10.0)
    
    def backwards(x, y):
        turtle.backward(10.0)

    def turnLeft(x,y):
        turtle.left(5.0)
    
    def turnRight(x,y):
        turtle.right(5.0)


    turtle.onclick(fun=forward, btn="w")
    turtle.onclick(fun=backwards, btn="s")

    screen = t.Screen()
    screen.exitonclick()

etch_a_sketch()