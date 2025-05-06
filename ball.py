from turtle import Turtle

class Ball(Turtle):
    def __init__(self, pos,shape = "classic", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 15
        self.y_move = 15
        self.speeds = 0.1
    
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)
    
    def y_bounce(self):
        self.y_move *= -1


    def x_bounce(self):
        self.x_move *= -1
        self.speeds *= 0.9

    def reset(self):
        self.goto(0,0)
        self.x_bounce()
        self.speeds = 0.1
