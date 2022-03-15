from turtle import *


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.score = 0

        with open("data.txt") as data:
            try:
                self.highscore = int(data.read())
            except ValueError:
                self.highscore = 0

        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0,280)
        self.update()

    def update(self):
        self.clear()
        self.write(f"score = {self.score}  highscore = {self.highscore}", False, align="center", font=("times new roman", 12, "bold"))

    def increase_score(self):
        self.score += 1
        # self.clear()
        self.update()

    def reset(self):
        if self.score >= self.highscore:
            self.highscore = self.score
            with open("data.txt",mode = "w") as data:
                data.write(f"{self.highscore}")

        self.score = 0
        self.update()

