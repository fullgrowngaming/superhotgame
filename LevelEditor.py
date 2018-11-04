import pygame
from Editor.EditorWindow import EditorWindow
from Editor.Room import Room
from tkinter import *

window = EditorWindow(240, 144)
clock = pygame.time.Clock()

room1 = Room.Deserialize('Levels/level.json')

brush = 64
loadedRoom = room1
activeLayer = room1.layers[0]

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
                loadedRoom.save()
                pygame.quit()
                sys.exit()

        mouse = pygame.mouse.get_pos()
        mouse_x = mouse[0]
        mouse_y = mouse[1]

        tile_x = mouse_x // loadedRoom.sprite_sheet.tile_width
        tile_y = mouse_y // loadedRoom.sprite_sheet.tile_height

        mouse_down = pygame.mouse.get_pressed()
        if mouse_down[0]:
            if tile_x <= loadedRoom.width and tile_y <= loadedRoom.height:
                activeLayer.SetTile(tile_x, tile_y, brush)

        for x in range(0, loadedRoom.width):
            for y in range(0, loadedRoom.height):
                tile = activeLayer.tiles[y][x]
                xloc = x * loadedRoom.sprite_sheet.tile_width
                yloc = y * loadedRoom.sprite_sheet.tile_height
                window.window.blit(tile, (xloc, yloc))

        update()


if __name__ == "__main__":
    window.tilePalette.ChangeSpriteSheet(room1.sprite_sheet.file, 24, 24)
    game_loop()
    room1.save()
