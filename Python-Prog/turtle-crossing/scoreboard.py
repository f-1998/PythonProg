from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(-230, 260)
        self.hideturtle()
        self.write(f"LEVEL:{self.score}", align="center", font=FONT)

    def level_up(self):
        self.score += 1
        self.clear()
        self.write(f"LEVEL:{self.score}", align="center", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)

