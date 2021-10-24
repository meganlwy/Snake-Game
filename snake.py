from turtle import Screen, Turtle


STARTINGPOSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVEDISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snakebody = []
        self.createsnake()
        self.head = self.snakebody[0]

    def createsnake(self):
        for n in STARTINGPOSITIONS:
            self.addbody(n)

    def addbody(self, n):
        newsnake = Turtle("square")
        newsnake.penup()
        newsnake.speed("fast")
        newsnake.goto(n)
        newsnake.color("white") 
        self.snakebody.append(newsnake)

    def extendtail(self):
        self.addbody(self.snakebody[-1].position())

    def snakemove(self):
        for body in range(len(self.snakebody) - 1, 0, -1):
            newx = self.snakebody[body - 1].xcor()
            newy = self.snakebody[body - 1].ycor()
            self.snakebody[body].goto(newx, newy)
        self.head.forward(MOVEDISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
