import pygame

pygame.mixer.init()

laser_sound = pygame.mixer.Sound("shoot.wav")
explode_sound = pygame.mixer.Sound("explode.wav")
lose_sound = pygame.mixer.Sound("lose.wav")
win_sound = pygame.mixer.Sound("win.wav")