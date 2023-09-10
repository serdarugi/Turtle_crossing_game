FONT = ("Courier", 24, "normal")
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.level = 1
        self.penup()
        self.hideturtle()
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.goto(0, 250)
        self.write(f"Level : {self.level}",  align="center", font=FONT)


    def increase_level(self):
        self.level += 1
        self.update_scoreboard()


    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER ! Your Score : {self.level}", align="center", font=FONT)