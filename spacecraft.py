from turtle import Turtle
from sounds import laser_sound, explode_sound
from settings import *



class SpaceCraft(Turtle):

    def __init__(self, x, y):

        super().__init__()
        self.up()
        self.lives = 3
        self.goto(x, y)
        self.shape('spacecraft.gif')


    def move_right(self):
        if self.xcor() < BORDER_R:
            new_x = self.xcor() + 20
            self.goto(new_x, self.ycor())


    def  move_left(self):
        if self.xcor() > BORDER_L:
            new_x = self.xcor() - 20
            self.goto(new_x, self.ycor())


class Barrier(Turtle):

    def __init__(self, x, y):

        super().__init__()
        self.color('yellow')
        self.shape('square')
        self.up()
        self.goto(x, y)


class Laser(Turtle):

    def __init__(self):

        super().__init__()
        self.color('red')
        self.up()
        self.shape('square')
        self.shapesize(0.15, 0.6)
        self.lt(90)
        self.goto(800, 800)
        self.loaded = True


    def shoot(self, spacecraft):

        if self.loaded:
            laser_sound.play()
            self.goto(spacecraft.xcor(), spacecraft.ycor()+10)
            self.loaded = False


    def move(self):

        if not self.loaded:

            if self.ycor() <= 240:
                self.sety(self.ycor() + 20)
            else:
                self.goto(800, 800)
                self.loaded = True


    def hit_barrier(self, barrier_list):

        for barrier in barrier_list:
            if self.distance(barrier)<=15:
                explode_sound.play()
                self.goto(800,800)
                barrier.goto(800,800)
                barrier_list.remove(barrier)
                self.loaded = True


    def hit_invader(self, invader_list, board):

        for invader in invader_list:
            if self.distance(invader)<20:
                explode_sound.play()
                self.goto(800,800)
                invader.goto(800,800)
                invader_list.remove(invader)
                board.score += 1
