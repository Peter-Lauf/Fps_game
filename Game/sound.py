import pygame as pg


class Sound:
    def __init__(self, game):
        self.game = game
        pg.mixer.init()
        self.path = 'resources/sound/'
        self.assault_rifle = pg.mixer.Sound(self.path + 'assault_rifle.wav')