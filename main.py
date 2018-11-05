import pygame, time, sys, random
from GameWindow import GameWindow
from Player import *
from Editor.Room import Room
from Renderer import Renderer

import json

pygame.init()
window = GameWindow(240, 135)
player = Player(50,50)
effect = Effect(player)
clock = pygame.time.Clock()
room1 = Room('Levels/level.json')
renderer = Renderer(window)
renderer.all_sprites.add(player, player.sword, player.shield, effect)

def update():
    window.display()
    clock.tick(60)
    print(player.attack_anim_timer, player.walking, player.direction, player.defending)


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
        if pressed[pygame.K_LSHIFT]:
            player.defend()
        elif pressed[pygame.K_LEFT]:
            player.defending = False
            player.move(3)
        elif pressed[pygame.K_RIGHT]:
            player.defending = False
            player.move(1)
        elif pressed[pygame.K_UP]:
            player.defending = False
            player.move(0)
        elif pressed[pygame.K_DOWN]:
            player.defending = False
            player.move(2)
        else:
            player.walking = False
            player.defending = False
            player.move(4)  # if you stop moving (i.e. not holding a direction)

        # draw sprites and update window
        player.update()
        player.sword.update()
        player.shield.update()
        effect.update()

        renderer.draw()
        update()


if __name__ == "__main__":
    game_loop()
    room1.save()
