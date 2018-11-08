import pygame
import os
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from Editor.TilePalette import TilePalette
from Editor.LayerSelector import LayerSelector


class EditorWindow:
    '''Creates and maintains the game window'''
    white = (255,255,255)

    def __init__(self, window_res_x, window_res_y, viewModel):
        self.res_x = window_res_x
        self.res_y = window_res_y
        self.viewModel = viewModel

        self.root = tk.Tk()

        self.layerSelector = LayerSelector(self.root, viewModel, width=80)
        self.layerSelector.pack(side=LEFT)

        self.tilePalette = TilePalette(self.root, viewModel, width=80)
        self.tilePalette.pack(side=RIGHT)

        embed = tk.Frame(self.root, width=240, height=144)  # creates embed
        # frame for pygame
        #embed.grid(columnspan=600, rowspan=500)  # Adds grid
        embed.pack(side=LEFT)  # packs window to the left

        os.environ['SDL_WINDOWID'] = str(embed.winfo_id())
        os.environ['SDL_VIDEODRIVER'] = 'windib'

        self.window = pygame.display.set_mode((window_res_x, window_res_y))
        pygame.display.set_caption('Level Editor Util')

        self.background = pygame.Surface(self.window.get_size())
        self.background = self.background.convert()
        self.background.fill((250, 250, 250))

        pygame.display.init()

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.display()

    def on_closing(self):
        if messagebox.askokcancel("Save", "Do you want to save?"):
            self.viewModel.loadedRoom.save()
        self.root.destroy()

    def display(self):
        pygame.display.update()
        self.root.update()
