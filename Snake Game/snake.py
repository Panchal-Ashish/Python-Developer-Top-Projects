from turtle import *
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.head.color("green")


    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
            # creates our starting snake

    def reset(self):
        for segment in self.segments:
            segment.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        ## this function will be called when snake eats food,
        ## so the new segment needs to be added to the position of the last segment... i.e -1 index
        self.add_segment(self.segments[-1].position())


    def move(self):
        for seg in range((len(self.segments) - 1), 0, -1):
            ## making a particular segment to goto the position of the previous segment... like 3 to 2, 2 to 1, 1 to new
            ## making the tail to follow the head
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:     # cant go up if it is already going down
            self.head.setheading(UP)
            # do not use left or right... coz it goes left/right relative to current position and not absolute position

    def down(self):
        if self.head.heading() != UP:       # cant go down if it is already going up
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:    # cant go left if it is already going right
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:     # cant go right if it is already going left
            self.head.setheading(RIGHT)
