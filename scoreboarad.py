from turtle import Turtle
FONT = ("Arial", 20, "bold")
ALIGN = "left"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(x=-350, y=275)
        self.level = 0
        self.update_scoreboard()

    def increase_level(self):
        """This function increases the level"""
        self.level += 1
        self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):
        """This function updates the scoreboard"""
        self.write(f"Current Level: {self.level}", align=ALIGN, font=FONT)
