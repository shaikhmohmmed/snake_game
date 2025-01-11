from turtle import  Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTACE = 20
Up = 90
Down = 270
Left = 180
Right = 0
class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        segment_1 = Turtle("circle")
        segment_1.color("white")
        segment_1.penup()
        segment_1.goto(position) 
        self.segments.append(segment_1)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
    def extend(self):
        self.add_segment(self.segments[-1].position())
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTACE)


    def up(self):
        if self.head.heading() != Down:
             self.head.setheading(Up)
    def down(self):
        if self.head.heading() != Up:
            self.head.setheading(Down)
    def left(self):
        if self.head.heading() != Right:
            self .head.setheading(Left)
    def right(self):
        if self.head.heading() != Left:
            self.head.setheading(Right)

