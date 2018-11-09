import pygame
from Camera import Camera

class Renderer():
    def __init__(self, Camera, GameWindow):
        #should be able to handle layering somehow, haven't worked that out yet
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.window = GameWindow
        self.camera = Camera


    def draw(self):
        for sprite in self.all_sprites:
            self.window.window.blit(sprite.image, (sprite.rect.x - (self.camera.rect.x * self.window.res_x), sprite.rect.y - (self.camera.rect.y * self.window.res_y)))
