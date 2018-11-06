import pygame

class Renderer():
    def __init__(self, GameWindow):
        #should be able to handle layering somehow, haven't worked that out yet
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.window = GameWindow

    def draw(self):
        for sprite in self.all_sprites:
            self.window.window.blit(sprite.image, (sprite.rect.x, sprite.rect.y))
