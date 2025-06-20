from turtle import Turtle
from settings import *


class Board(Turtle):

    def __init__(self):

        super().__init__()
        self.up()
        self.ht()
        self.color('white')
        self.score = 0


    def update(self, dummy_list):

        self.clear()
        self.place_dummies(dummy_list)
        self.goto(SCORE_X, SCORE_Y)
        self.write(f'Score: {self.score}', font=R_FONT)


    def place_dummies(self, dummy_list):

        x = LIVES_X
        y = LIVES_Y

        for dummy in dummy_list:
            dummy.goto(x, y)
            x += 50


    def game_over(self):

        self.goto(0,0)
        self.write('GAME OVER', align='center', font=GO_FONT)


class Dummy(Turtle):

    def __init__(self):

        super().__init__()
        self.shape('spacecraft.gif')
        self.up()
        self.goto(800, 800)
