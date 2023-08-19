from turtle import Turtle

t = Turtle()


class Snake:

    START_POSITION = [(0, 0), (-20, 0), (-40, 0)]
    MOVE_DISTANCE = 20
    UP = 90
    DOWN = 270
    RIGHT = 0
    LEFT = 180

    def __init__(self):
        self.segs = []

        self.create_snake()
        self.head = self.segs[0]

    def create_snake(self):
        for position in Snake.START_POSITION:
            self.add_seg(position)

    def add_seg(self, position):
        seg = Turtle("square")
        seg.color("white")
        seg.up()
        seg.goto(position)
        self.segs.append(seg)

    def extend(self):
        self.add_seg(self.segs[-1].position())

    def turn(self):
        for i in range(len(self.segs)-1, 0, -1):
            newx = self.segs[i - 1].xcor()
            newy = self.segs[i - 1].ycor()
            self.segs[i].goto(newx, newy)
        self.head.forward(Snake.MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != Snake.DOWN:
            self.head.setheading(Snake.UP)

    def down(self):
        if self.head.heading() != Snake.UP:
            self.head.setheading(Snake.DOWN)

    def right(self):
        if self.head.heading() != Snake.LEFT:
            self.head.setheading(Snake.RIGHT)

    def left(self):
        if self.head.heading() != Snake.RIGHT:
            self.head.setheading(Snake.LEFT)
