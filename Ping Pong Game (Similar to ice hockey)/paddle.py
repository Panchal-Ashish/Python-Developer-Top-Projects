from turtle import *


class Paddle(Turtle):
    def __init__(self, go_to_position):
        super(Paddle, self).__init__()
        self.shape("square")    # rectangle is not directly available, so using square and then changing its dimensions
        self.shapesize(stretch_wid=5, stretch_len=1)  # 1 sq is 20 x 20... we need rect with horizontal = 20, vertical = 100
        self.color("white")
        self.penup()
        self.goto(go_to_position)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    # def __init__(self):
    #     self.x_pos = 350
    #     self.y_pos = -50
    #     self.segments = []
    #     self.create_paddle()
    #
    # def create_paddle(self):
    #     for _ in range(0,5):
    #         new_segment = Turtle("square")
    #         new_segment.color("white")
    #         new_segment.penup()
    #         new_segment.goto(self.x_pos, self.y_pos)
    #         self.y_pos += 20
    #         self.segments.append(new_segment)



