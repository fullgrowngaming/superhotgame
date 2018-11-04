import pygame
import os
import tkinter as tk
from tkinter import *
from Editor.TilePalette import TilePalette

class EditorWindow:
    '''Creates and maintains the game window'''
    white = (255,255,255)

    def __init__(self, window_res_x, window_res_y):
        self.res_x = window_res_x
        self.res_y = window_res_y

        self.root = tk.Tk()
        self.tilePalette = TilePalette(self.root, width=200, height=300)
        self.tilePalette.grid(row=0, column=1)

        embed = tk.Frame(self.root, width=240,
                         height=144)  # creates embed frame for pygame
        embed.grid(columnspan=600, rowspan=500)  # Adds grid
        #embed.pack(side=LEFT)  # packs window to the left

        os.environ['SDL_WINDOWID'] = str(embed.winfo_id())
        os.environ['SDL_VIDEODRIVER'] = 'windib'

        self.window = pygame.display.set_mode((window_res_x, window_res_y))
        self.window.fill(pygame.Color(0, 0, 0))

        pygame.display.set_caption('Level Editor Util')

        pygame.display.init()

        self.display()

    def display(self):
        pygame.display.update()
        self.root.update()