import pygame

class Level:
    def __init__(self):
        self.collision = pygame.image.load('Game/collision.png')
        self.mask = pygame.mask.from_surface(self.collision)
        self.image = pygame.image.load('Game/level.png')
        self.rect = self.image.get_rect()
        self.background_music = pygame.mixer.Sound('Game/bg.ogg')
        self.background_music.play()

class LevelOverlay:
    def __init__(self):
        self.image = pygame.image.load('Game/overlay.png')
        self.rect = self.image.get_rect()
