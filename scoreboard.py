from turtle import Turtle
# Score board font.
FONT = ('courier', 20, 'normal')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()

        self.score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 270)
        # self.current_score()
        self.write(arg=f"Score: {self.score}", align="center", font=FONT)

    def current_score(self):
        self.clear()
        self.score += 1
        self.write(arg=f"Score: {self.score}", align="center", font=FONT)

    def game_over(self):
        self.home()
        self.write(arg="GAME OVER!", align="center", font=FONT)

