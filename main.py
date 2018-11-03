import pygame, time, sys, random
from GameWindow import GameWindow
from Player import Player
from Editor.Room import Room
from Renderer import Renderer

import json

pygame.init()
window = GameWindow(240, 135)
player = Player(50,50)
clock = pygame.time.Clock()
room1 = Room('Levels/level.json')
renderer = Renderer(window)
renderer.all_sprites.add(player)

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

        # handles keypresses and moves the player
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_SPACE] and player.attack_cooldown == 0:
            player.attack()
        elif pressed[pygame.K_LEFT]:
            player.move(3)
        elif pressed[pygame.K_RIGHT]:
            player.move(1)
        elif pressed[pygame.K_UP]:
            player.move(0)
        elif pressed[pygame.K_DOWN]:
            player.move(2)
        else:
            player.move(4)  # if you stop moving (i.e. not holding a direction)

        # draw sprites and update window
        player.update()
        renderer.draw()
        update()


if __name__ == "__main__":
    game_loop()
    room1.save()
