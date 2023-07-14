from turtle import Turtle

MOVE_DISTANCE = 20

class Snake:
    def __init__(self):
        body = []
        for index in range(3):
            square = Turtle(shape="square")
            square.penup()
            square.color("white")
            square.setx(square.pos()[0] - ((index + 1) * MOVE_DISTANCE))
            body.append(square)

        self.body = body

    def move(self):
        for seg_id in range(len(self.body) -1, 0, -1):
            new_x = self.body[seg_id - 1].xcor()
            new_y = self.body[seg_id - 1].ycor()
            self.body[seg_id].goto(new_x, new_y)
        self.body[0].forward(MOVE_DISTANCE)

    def up(self):
        self.body[0].setheading(90)

    def down(self):
        self.body[0].setheading(270)

    def left(self):
        self.body[0].setheading(180)
    
    def right(self):
        self.body[0].setheading(0)