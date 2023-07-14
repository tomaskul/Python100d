from turtle import Turtle
from random import randint

class Food(Turtle):
    def __init__(self):
        super().__init__("circle")
        self.penup()
        self.color("red")
        self.shapesize(0.5, 0.5, 0.5)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = randint(-280, 280)
        random_y = randint(-280, 260)
        self.goto(random_x, random_y)