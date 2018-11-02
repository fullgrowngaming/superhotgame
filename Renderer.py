import pygame
from GameWindow import GameWindow

class Renderer():
    def __init__(self, GameWindow):
        #should be able to handle layering somehow, haven't worked that out yet
        self.sprites_list = pygame.sprite.LayeredUpdates()
        self.Window = GameWindow

    def draw(self):
        for sprite in self.sprites_list:
            self.Window.window.blit(sprite.current_frame, (sprite.x, sprite.y))
