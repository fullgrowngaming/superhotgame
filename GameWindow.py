import pygame

class GameWindow:
    '''Creates and maintains the game window'''
    white = (255,255,255)

    def __init__(self, window_res_x, window_res_y):
        self.res_x = window_res_x
        self.res_y = window_res_y
        self.window = pygame.display.set_mode((window_res_x, window_res_y))
        self.window.fill(GameWindow.white)
        pygame.display.set_caption('UNTITLED GAME WITH 32')
        self.display()

    def display(self):
        pygame.display.update()