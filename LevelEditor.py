import pygame
from Editor.EditorWindow import EditorWindow
from Editor.RoomEditorViewModel import RoomEditorViewModel
from Editor.Room import Room
from tkinter import *

viewModel = RoomEditorViewModel()
viewModel.currentBrush = 3

window = EditorWindow(240, 144, viewModel)
clock = pygame.time.Clock()

room1 = Room.Deserialize('Levels/level.json')
viewModel.loadedRoom = room1
viewModel.activeLayer = room1.layers[0]

tileBrushes = []

def update():
    clock.tick(60)
    window.display()

def game_loop():
    running = True
    while running:
        #handle quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        mouse = pygame.mouse.get_pos()
        mouse_x = mouse[0]
        mouse_y = mouse[1]

        tile_x = mouse_x // viewModel.loadedRoom.sprite_sheet.tile_width
        tile_y = mouse_y // viewModel.loadedRoom.sprite_sheet.tile_height

        mouse_down = pygame.mouse.get_pressed()
        if mouse_down[0]:
            if tile_x <= viewModel.loadedRoom.width and tile_y <= viewModel.loadedRoom.height:
                viewModel.activeLayer.SetTile(tile_x, tile_y, viewModel.currentBrush)

        for x in range(0, viewModel.loadedRoom.width):
            for y in range(0, viewModel.loadedRoom.height):
                tile = viewModel.activeLayer.tiles[y][x]
                xloc = x * viewModel.loadedRoom.sprite_sheet.tile_width
                yloc = y * viewModel.loadedRoom.sprite_sheet.tile_height
                window.window.blit(tile, (xloc, yloc))

        update()


if __name__ == "__main__":
    window.tilePalette.ChangeSpriteSheet(room1.sprite_sheet.file, 24, 24)
    game_loop()
    room1.save()
