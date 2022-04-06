from turtle import Turtle

class Middle_line(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('square')
        self.hideturtle()
        #self.shapesize(10, 1)
        self.penup()
        self.goto(0,335)


    def draw_middle(self):
        self.setheading(270)
        self.pensize(5)
        for i in range(19):
            self.forward(20)
            self.penup()
            self.forward(20)
            self.pendown()
