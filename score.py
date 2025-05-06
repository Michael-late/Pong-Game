from turtle import Turtle

class Score(Turtle):
    def __init__(self,LScore, RScore, shape = "classic", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)
        self.color("white")
        self.penup()
        self.rscore = RScore
        self.lscore = LScore
        self.hideturtle()
        self.update()
       

    def rAdd(self):
        self.rscore += 1
        self.update()

    def lAdd(self):
        self.lscore += 1
        self.update()

    def update(self):
        self.clear()
        self.goto(-20,200)
        self.write(f"{self.lscore} : {self.rscore}", font=("Arial", 20, "normal"))