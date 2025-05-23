from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt" , mode="r") as f :
            self.highscore = int(f.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} HIGH SCORE : {self.highscore}", align=ALIGNMENT, font=FONT)

    def reset(self) :
        if self.score > self.highscore :
            self.highscore = self.score
        self.score = 0 
        self.update_scoreboard()
        with open("data.txt" , mode="w") as f :
            f.write(str(self.highscore))
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
