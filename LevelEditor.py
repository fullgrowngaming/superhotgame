import pygame, time, sys, random
from GameWindow import GameWindow
from Player import Player
from Editor.Room import Room

import json

pygame.init()
window = GameWindow(240, 135)
clock = pygame.time.Clock()
room1 = Room('Levels/level.json')

def update():
    window.display()
    clock.tick(60)

def game_loop():
    running = True
    while running:
        window.window.fill(GameWindow.white)

        #handle quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        for layer in room1.layers:
            for x in range(0, room1.width):
                for y in range(0, room1.height):
                    tile = layer.tiles[y][x]
                    xloc = x * room1.sprite_sheet.tile_width
                    yloc = y * room1.sprite_sheet.tile_height
                    window.window.blit(tile, (xloc, yloc))

        update()


if __name__ == "__main__":
    game_loop()
    room1.save()
