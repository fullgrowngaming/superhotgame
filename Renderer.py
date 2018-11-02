import pygame
from GameWindow import GameWindow

class Renderer():
    def __init__(self):
        #should be able to handle layering somehow, haven't worked that out yet
        self.sprites_list = pygame.sprite.LayeredUpdates()

    def draw(self, GameWindow):
        for sprite in self.sprites_list:
            GameWindow.window.blit(sprite.current_frame, (sprite.x, sprite.y))
