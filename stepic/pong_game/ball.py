from turtle import Turtle

class Ball(Turtle):
    def __init__(self, position):
        super().__init__()  # Using super to inherit from Turtle class
        self.shape('circle')
        self.shapesize()
        self.color('pink')
        self.penup()
        self.goto(position)
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1

    def paddle_bounce(self):
        self.x_move *= -1
