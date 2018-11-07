from Editor.TileTable import TileTable
import PIL.Image, PIL.ImageTk
import tkinter as tk
from tkinter import *


class TilePalette(tk.Frame):
    def __init__(self, root, vm, **kwargs):
        super(TilePalette, self).__init__(root, kwargs)
        self.vm = vm

        self.preview = tk.Canvas(self, height=100)
        self.preview.pack(side=TOP, expand=True, fill=Y)

        self.canvas = tk.Canvas(self, scrollregion=(0, 0, 30, 600))
        hbar = tk.Scrollbar(self, orient=HORIZONTAL)
        hbar.pack(side=BOTTOM, fill=X)
        hbar.config(command=self.canvas.xview)

        vbar = tk.Scrollbar(self, orient=VERTICAL)
        vbar.pack(side=RIGHT, fill=Y)
        vbar.config(command=self.canvas.yview)

        self.canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
        self.canvas.pack(side=BOTTOM, expand=True, fill=BOTH)

        self.canvas.bind('<Button-1>', self.click)

        self.tile_height = None
        self.tile_width = None

        self.tkTiles = []
        self.tileBrushes = []

        self.tkPreview = None
        self.selected = None
        self.selectedPreview = None
        self.padding = 5

    def click(self, event):
        x, y = event.x, event.y
        x = self.canvas.canvasx(x)
        y = self.canvas.canvasy(y)

        index = self.GetClickedSpriteIndex(x, y)

        self.vm.currentBrush = index

    def GetClickedSpriteIndex(self, x, y):
        region_x = self.padding + self.tile_width
        region_y = self.padding + self.tile_height

        width = self.canvas.winfo_width()
        perRow = width // region_x

        region_x = x // region_x
        region_y = y // region_y

        index = perRow * region_y + region_x

        rectx = region_x * (self.tile_width + self.padding) - 1 + self.padding
        recty = region_y * (self.tile_height + self.padding) - 1 + self.padding

        if self.selected is not None:
            self.canvas.delete(self.selected)

        self.selected = self.canvas.create_rectangle(rectx, recty, rectx +
                                           self.tile_width,
                                     recty + self.tile_height, outline='red')

        if self.selectedPreview is not None:
            self.preview.delete(self.selectedPreview)

        previewImage = self.tileBrushes[int(index)]
        previewImage = previewImage.resize((50, 50))
        self.tkPreview = PIL.ImageTk.PhotoImage(previewImage)

        self.selectedPreview = self.preview.create_image(
            self.preview.winfo_width() / 2, self.preview.winfo_height() / 2,
            image=self.tkPreview)
        return int(index)

    def ChangeSpriteSheet(self, file, tile_width, tile_height):
        self.tileBrushes.clear()
        self.tkTiles.clear()

        self.tile_width = tile_width
        self.tile_height = tile_height

        sprite_sheet = TileTable(file, tile_width, tile_height)

        pilImage = PIL.Image.open(sprite_sheet.file)

        image_width, image_height = pilImage.size

        self.tile_count_x = image_width // tile_width
        self.tile_count_y = image_height // tile_height

        for tile_y in range(0, self.tile_count_y):
            for tile_x in range(0,self.tile_count_x):
                x = tile_x * tile_width
                y = tile_y * tile_height
                cropped = pilImage.crop((x, y, x + tile_width, y + tile_height))
                self.tileBrushes.append(cropped)

        self.DrawTiles()
        return

    def DrawTiles(self):
        y = self.padding
        x = self.padding
        width = self.canvas.winfo_width()

        for tile in self.tileBrushes:
            tkImage = PIL.ImageTk.PhotoImage(tile)
            self.tkTiles.append(tkImage)
            sprite = self.canvas.create_image(x, y, image=tkImage, anchor="nw")

            x += self.tile_width + self.padding

            # wrap
            if x + self.tile_width > width:
                x = self.padding
                y += self.tile_height + self.padding

        self.canvas.config(scrollregion=(0, 0, width, y))
        self.canvas.update()
