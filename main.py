from turtle import Screen
from sounds import *
from invader import *
from spacecraft import *
from board import *
import time

class App:

    def __init__(self):

        super().__init__()

        # ---- setting the screen ---- #
        self.screen = Screen()
        self.screen.title('Space Invaders')
        self.screen.setup(width=WIDTH, height=HEIGHT)
        self.screen._root.resizable(False, False)
        self.screen.bgcolor('black')

        # ---- some new shapes ---- #
        self.screen.tracer(0)
        self.screen.addshape('invader1.gif')
        self.screen.addshape('invader2.gif')
        self.screen.addshape('spacecraft.gif')

        # ---- objects ---- #
        self.player = SpaceCraft(I_POSX, I_POSY)
        self.board = Board()
        self.invader_list = []
        self.barrier_list = []
        self.live_list = []
        self.load_lives()
        self.place_invaders()
        self.place_barriers()
        self.place_lives()
        self.laser = Laser()
        self.bomb = Bomb()

        # ---- setting the keyboard ---- #
        self.screen.listen()
        self.screen.onkey(self.player.move_right, 'Right')
        self.screen.onkey(self.player.move_left, 'Left')
        self.screen.onkey(self.player_shoot, 'space')
        self.screen.onscreenclick(self.get_coords)

        # ---- starting the game ---- #
        self.game_is_on = True
        self.lets_play()

        self.screen.mainloop()


    def get_coords(self, x, y):
        print(f"Clic en: ({int(x)}, {int(y)})")


    def lets_play(self):

        count = 1
        while self.game_is_on:

            count += 1
            self.board.update(self.live_list)
            self.check_others()
            self.screen.update()
            self.bomb.drop(self.invader_list)
            self.bomb.move()
            self.laser.move()
            self.laser.hit_barrier(self.barrier_list)
            self.laser.hit_invader(self.invader_list, self.board)
            self.bomb.hit_barrier(self.barrier_list)
            if self.bomb.hit_spacecraft(self.player):
                if self.player.lives > 0:
                    live_lost = self.live_list[-1]
                    live_lost.goto(800,800)
                    self.live_list.remove(live_lost)
                    self.player.goto(I_POSX, I_POSY)
                else:
                    lose_sound.play()
                    self.game_over()
            self.move_invaders(count)
            time.sleep(0.02)


    def game_over(self):

        self.board.game_over()
        time.sleep(0.02)
        self.game_is_on = False



    def player_shoot(self):

        self.laser.shoot(self.player)


    def place_invaders(self):

        x = IX
        y = IY
        for _ in range(ROWS):
            for _ in range(I_ROW):
                new_invader = Invader(x,y)
                self.invader_list.append(new_invader)
                x += 50
            y += 50
            x = IX


    def place_barriers(self):

        for y in BARRIERS_Y:

            for x in BARRIERS_X:

                new_barrier = Barrier(x,y)
                self.barrier_list.append(new_barrier)


    def place_lives(self):

        self.board.place_dummies(self.live_list)


    def load_lives(self):

        for _ in range(self.player.lives):
            new_live = Dummy()
            self.live_list.append(new_live)


    def move_invaders(self, count):

        for invader in self.invader_list:
            invader.move(count, self.invader_list)


    def check_others(self):

        for invader in self.invader_list:
            if invader.ycor() <= I_POSY + 10:
                lose_sound.play()
                self.game_over()

        if len(self.invader_list) == 0:
            win_sound.play()
            self.game_over()


App().lets_play()


