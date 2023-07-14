from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__(visible=False)
        self.color("white")
        self.speed("fastest")
        self.goto(0.0, 280)

        self.score = 0
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(arg=f"SCORE: {self.score}", move=False, align="center", font=("Helvetica", 12, "normal"))

    def increment_score(self):
        self.score += 1
        self.write_score()
        