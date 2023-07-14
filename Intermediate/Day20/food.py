from turtle import Turtle

class Food(Turtle):
    def __init__(self):
        super().__init__("circle")
        self.color("red")
        self.shapesize(0.5, 0.5, 0.5)