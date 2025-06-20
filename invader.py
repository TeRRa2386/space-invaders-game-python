from turtle import Turtle
from random import random
from sounds import explode_sound


class Invader(Turtle):

    def __init__(self, x, y):

        super().__init__()
        self.up()
        self.goto(x, y)
        self.x_direction = 1
        self.shape('invader1.gif')


    def move(self, counter, invader_list):

        self.goto(self.xcor() + self.x_direction, self.ycor())
        self.animation(counter)

        if self.xcor() >= 240 or self.xcor() <= -240:
            for invader in invader_list:
                invader.x_direction *= -1
                invader.sety(invader.ycor() - 30)


    def animation(self, counter):

        if counter%20 == 0:
            if self.shape() == 'invader1.gif':
                self.shape('invader2.gif')
            else:
                self.shape('invader1.gif')


class Bomb(Turtle):

    def __init__(self):

        super().__init__()
        self.color('white')
        self.up()
        self.shapesize(0.15, 0.6)
        self.lt(90)
        self.goto(800, 800)
        self.loaded = True


    def drop(self, invader_list):
        for invader in invader_list:
            x = random()
            if x < 0.2 and self.loaded:
                self.loaded = False
                self.goto(invader.xcor(), invader.ycor()-20)


    def move(self):
        if not self.loaded:
            if self.ycor()>= -220:
                self.sety(self.ycor()-5)
            else:
                self.goto(800,800)
                self.loaded = True


    def hit_barrier(self, barrier_list):

        for barrier in barrier_list:
            if self.distance(barrier) <= 15:
                explode_sound.play()
                self.goto(800, 800)
                barrier.goto(800, 800)
                barrier_list.remove(barrier)
                self.loaded = True


    def hit_spacecraft(self, player):

        if self.distance(player) < 20:
            explode_sound.play()
            self.goto(800, 800)
            player.goto(800, 800)
            self.loaded = True
            player.lives -= 1
            return True
        else:
            return False