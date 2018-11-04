from Editor.TileTable import TileTable
import PIL.Image, PIL.ImageTk
import tkinter as tk
from tkinter import *


class TilePalette(tk.Frame):
    def __init__(self, root, **kwargs):
        super(TilePalette, self).__init__(root, kwargs)
        self.canvas = tk.Canvas(self, width=100, height=100, scrollregion=(
            0, 0, 30, 600))

        hbar = tk.Scrollbar(self, orient=HORIZONTAL)
        hbar.pack(side=BOTTOM, fill=X)
        hbar.config(command=self.canvas.xview)

        vbar = tk.Scrollbar(self, orient=VERTICAL)
        vbar.pack(side=RIGHT, fill=Y)
        vbar.config(command=self.canvas.yview)

        self.canvas.config(width=300, height=200)
        self.canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
        self.canvas.pack(side=LEFT, expand=True, fill=BOTH)

        self.tileBrushes = []

    def ChangeSpriteSheet(self, file, tile_width, tile_height):
        self.tileBrushes.clear()

        sprite_sheet = TileTable(file, tile_width, tile_height)

        pilImage = PIL.Image.open(sprite_sheet.file)
        image = PIL.ImageTk.PhotoImage(pilImage)

        height = image.height()
        width = image.width()

        x = 0
        y = 0

        while y <= height:
            while x <= width:
                cropped = pilImage.crop((x, y, x + tile_width, y + tile_height))
                image = PIL.ImageTk.PhotoImage(cropped)
                self.tileBrushes.append(image)

                x += tile_width
            x = 0
            y += tile_height

        y = 0

        height = len(self.tileBrushes * (tile_height + 5))
        self.canvas.config(scrollregion=(0, 0, 100, height))

        for tile in self.tileBrushes:
            sprite = self.canvas.create_image(0, y, image=tile)
            y += tile_height + 5
