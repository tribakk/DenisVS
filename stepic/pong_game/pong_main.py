from turtle import Screen
from puddle import Paddle
from ball import Ball
from scoreboard import Score
from centre_line import Middle_line
import time

screen = Screen()
screen.title('Pong Game')
screen.bgcolor('black')
screen.setup(800,600)
screen.tracer(0) #We update screen manually (with 'screen.update') after we draw initital objects such as paddles and ball
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

screen.listen()

screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

ball = Ball((0,0))
l_score = Score((-60, 245))
l_score.show_scoreboard()
r_score = Score((60, 245))
r_score.show_scoreboard()
line = Middle_line()
line.draw_middle()

x = 0.1 # Default animation speed

game_is_on = True
while game_is_on:
    time.sleep(x) #Slow animation for each while loop
    screen.update()
    ball.move()

    #Detect collision with a wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    #Detect collision wath a paddle
    if (ball.xcor()> 335 and ball.distance(r_paddle) < 50) or (ball.xcor()< -335 and ball.distance(l_paddle) < 50):
        ball.paddle_bounce()
        if x > 0:
            x -= 0.01


    #Detect missed ball
    if ball.xcor() > 380:
        l_score.refresh()
        ball.goto((0,0))
        x = 0.1
    if ball.xcor() < -380:
        r_score.refresh()
        ball.goto((0, 0))
        x = 0.1

screen.exitonclick()