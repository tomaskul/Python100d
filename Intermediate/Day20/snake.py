from turtle import Turtle

MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.body = []
        for index in range(3):
            self.add_segment(x_pos=0 - ((index + 1) * MOVE_DISTANCE), y_pos=0)
        
        self.head = self.body[0]

    def add_segment(self, x_pos, y_pos):
        segment = Turtle(shape="square")
        segment.penup()
        segment.color("white")
        segment.setx(x_pos)
        segment.sety(y_pos)
        self.body.append(segment)

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

    def eat(self):
        last_x = self.body[len(self.body)-1].xcor()
        last_y = self.body[len(self.body)-1].ycor()
        self.add_segment(last_x, last_y)
