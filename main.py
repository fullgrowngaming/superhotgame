import pygame, time, sys, random
from GameWindow import GameWindow
from Player import *
from Editor.Room import Room
from Renderer import Renderer
from Camera import Camera

import json

pygame.init()
win_x, win_y = 240, 135
window = GameWindow(win_x, win_y)
player = Player(50,50)
effect = Effect(player)
clock = pygame.time.Clock()
room1 = Room('Levels/level.json')
renderer = Renderer(window)
renderer.all_sprites.add(player, player.sword, player.shield, effect)
camera = Camera(win_x, win_y)

def update():
    window.display()
    clock.tick(60)
    #print(player.attack_anim_timer, player.walking, player.direction, player.defending, player.attacking)
    print(f'Camera X,Y: {camera.rect.x},{camera.rect.y} | X,Y: {player.rect.x},{player.rect.y}')


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
            for x in range(0, 10):
                for y in range(0, 6):
                    x_1 = x + (10 * camera.rect.x)
                    y_1 = y + (6 * camera.rect.y)
                    tile = layer.tiles[y_1][x_1]
                    xloc = x * room1.sprite_sheet.tile_width
                    yloc = y * room1.sprite_sheet.tile_height
                    window.window.blit(tile, (xloc, yloc))

        # handles keypresses and moves the player
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_SPACE] and player.attack_cooldown == 0 and not player.defending:
            player.attack()
        if pressed[pygame.K_LSHIFT] and not player.attacking:
            player.defend()
        elif pressed[pygame.K_LEFT]:
            player.move(3)
        elif pressed[pygame.K_RIGHT]:
            player.move(1)
        elif pressed[pygame.K_UP]:
            player.move(0)
        elif pressed[pygame.K_DOWN]:
            player.move(2)
        else:
            player.walking = False
            player.move(4)  # if you stop moving (i.e. not holding a direction)

        if player.rect.right > win_x:
            camera.rect.x += 1
            player.rect.left = 0

        elif player.rect.left < 0:
            camera.rect.x -= 1
            player.rect.right = win_x


        # draw sprites and update window
        renderer.all_sprites.update()
        renderer.draw()
        update()


if __name__ == "__main__":
    game_loop()
    room1.save()
