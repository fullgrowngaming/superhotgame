import pygame

class Camera():
    def __init__(self, width, height):
        self.rect = pygame.Rect(0,0, width, height)