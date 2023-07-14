import turtle as t

class Snake:
    def __init__(self):
        body = []
        for index in range(3):
            square = t.Turtle(shape="square")
            square.penup()
            square.color("white")
            square.setx(square.pos()[0] - ((index + 1) * 20))
            body.append(square)

        self.body = body


snake = Snake()

screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Python Snake Game")

screen.exitonclick()