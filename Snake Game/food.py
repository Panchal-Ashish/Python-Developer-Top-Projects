from turtle import *
import random


class Food(Turtle):
    def __init__(self):

        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.shapesize(0.8)
        self.speed('fastest')
        self.refresh()
        # self.goto(random.randint(-280,280),random.randint(-280,280))

        ## without inheritance, without using super init , without passing Turtle inside food
        ## self.food = Turtle("circle")
        ## self.food.color("red")
        ## self.food.penup()
        ## self.food.shapesize(0.8)
        ## self.food.speed("fastest")
        ## self.food.goto(random.randint(-280, 280), random.randint(-280, 280))

    def refresh(self):
        self.goto(random.randint(-280, 280), random.randint(-280, 280))
