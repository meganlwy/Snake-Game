from turtle import Turtle

STYLE = ("Courier", 20, "normal")
SCOREPOSITION = (0, 270)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.score = 0
        self.goto(SCOREPOSITION)
        self.updatescoreboard()

    def updatescoreboard(self):
        self.write(f"Score: {self.score}", align="center", font=STYLE)

    def increasescore(self):
        self.score += 1
        self.updatescoreboard()

    def endgame(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", move=False, align="center", font=STYLE)
