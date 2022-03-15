# NOT SO IMPORTANT
from turtle import *


class Starting(Turtle):

    def __init__(self):
        super().__init__()
        self.color("White")
        self.hideturtle()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.speed("fastest")
        self.border()
        self.center_line()

    def border(self):
        self.speed("fastest")
        self.penup()
        self.goto(-390,290)
        self.pendown()
        self.goto(390,290)
        self.goto(390,-290)
        self.goto(-390,290)
        self.goto(-390,290)

    def center_line(self):
        self.speed("fastest")
        self.penup()
        self.goto(0,300)
        while self.ycor() >= -299:
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)

