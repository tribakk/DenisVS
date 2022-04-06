from turtle import Turtle

class Score(Turtle):

    def __init__(self, position):
        super().__init__()
        self.color('white')
        self.score_number = 0
        self.penup()
        self.goto(position)

    def show_scoreboard(self):
        self.hideturtle()
        self.write(f"{self.score_number}", False, align="center", font=('Arial', 52, 'bold'))

    def refresh(self):
        self.clear()
        self.up_score()
        self.show_scoreboard()

    def up_score(self):
        self.score_number +=1