from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()  # Using super to inherit from Turtle class
        self.shape('square')
        self.shapesize(5, 1)
        self.color('white')
        self.penup()
        self.goto(position)

    def up(self):
        new_y = self.ycor() + 20  # to go up we increase Y
        self.goto(self.xcor(), new_y) # we leave xcor as is

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)