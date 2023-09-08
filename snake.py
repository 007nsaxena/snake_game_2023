from turtle import Turtle
COORDINATES = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE = 20


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in COORDINATES:
            new_seg = Turtle('square')
            new_seg.color('green')
            new_seg.penup()
            new_seg.goto(position)
            self.segments.append(new_seg)

        print(self.segments)

    def move_snake(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].fd(DISTANCE)

    def up(self):

        self.segments[0].setheading(90)

    def down(self):

        self.segments[0].setheading(270)

    def left(self):

        self.segments[0].setheading(180)

    def right(self):

        self.segments[0].setheading(0)

    def add_snake(self):
        new_x = self.segments[len(self.segments)-1].xcor()
        new_y = self.segments[len(self.segments) - 1].ycor()
        new_seg = Turtle('square')
        new_seg.color('green')
        new_seg.penup()
        new_seg.goto(new_x, new_y)
        self.segments.append(new_seg)

    def check_wall(self):
        self.hit_wall = False
        for seg in self.segments:
            if seg.xcor() > 300 or seg.xcor() < -300 or seg.ycor() > 300 or seg.ycor() < -300:
                self.hit_wall = True

    def check_snake(self):
        self.hit_snake = False
        if self.head.xcor() == self.segments[len(self.segments) -1].xcor() and self.head.ycor() == self.segments[len(self.segments) -1 ].ycor():
            self.hit_snake = True
