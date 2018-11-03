import pygame

class Renderer():
    def __init__(self, GameWindow):
        #should be able to handle layering somehow, haven't worked that out yet
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.Window = GameWindow

    def draw(self):
        for sprite in self.all_sprites:
            self.Window.window.blit(sprite.image, (sprite.x, sprite.y))
