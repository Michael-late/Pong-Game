from turtle import Screen
from paddle import Paddle
from score import Score
from ball import Ball
import time

def rf():
    pos = Right_paddle.pos()
    Right_paddle.setpos(pos[0],pos[1]+20)

def rd():
    pos = Right_paddle.pos()
    Right_paddle.setpos(pos[0],pos[1]-20)


def lf():
    pos = Left_paddle.pos()
    Left_paddle.setpos(pos[0],pos[1]+20)

def ld():
    pos = Left_paddle.pos()
    Left_paddle.setpos(pos[0],pos[1]-20)

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pong")
screen.tracer(0,0)

screen.onkey(rf,"Up")
screen.onkey(rd,"Down")

screen.onkey(lf,"w")
screen.onkey(ld,"s")
screen.listen()

#paddle
Right_paddle = Paddle((350,0))
Left_paddle = Paddle((-350,0))

#ballz
ball = Ball((0,0))
score = Score(0,0)

while True:
    time.sleep(ball.speeds)
    screen.update()
    ball.move()
    

    #detect wall collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()
    
    #paddle collision
    if ball.distance(Right_paddle) < 50 and ball.xcor() > 320:
        ball.x_bounce()
    
    if ball.distance(Left_paddle) < 50 and ball.xcor() < -320:
        ball.x_bounce()
    
    #out of bound - scores
    elif ball.xcor() > 380:
        ball.reset()
        score.lAdd()
    
    elif ball.xcor() < -380:
        ball.reset()
        score.rAdd()
        


screen.exitonclick()
