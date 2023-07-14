from turtle import Turtle

MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

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
        self.head = body[0]

    def move(self):
        for seg_id in range(len(self.body) -1, 0, -1):
            new_x = self.body[seg_id - 1].xcor()
            new_y = self.body[seg_id - 1].ycor()
            self.body[seg_id].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)