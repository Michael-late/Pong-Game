from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,pos, shape = "classic", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x=pos[0], y=pos[1])
