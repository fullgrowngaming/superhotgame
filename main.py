import pygame, time, sys, random
from GameWindow import GameWindow
from Player import *
from Editor.Room import Room
from Renderer import Renderer
from Camera import Camera
import json
pygame.init()

WIN_X, WIN_Y = 240, 135

#OBJECTS
window = GameWindow(WIN_X, WIN_Y)
camera = Camera(WIN_X, WIN_Y)
player = Player(50,50)
effect = Effect(player)
clock = pygame.time.Clock()
room1 = Room('Levels/level.json')
renderer = Renderer(camera, window)

renderer.all_sprites.add(player, player.sword, player.shield, effect)

def update():
    window.display()
    clock.tick(60)
    print(f'Camera X,Y: {camera.rect.x},{camera.rect.y} | Player X,Y: {player.rect.x},{player.rect.y}'
          f' State: {player.state}, Speed: {player.speed}, Attack Cooldown: {player.anim_timer}')

def game_loop():
    running = True
    while running:
        #handle quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        #hardcoded, fix later #to-do
        for layer in room1.layers:
            for x in range(0, 10):
                for y in range(0, 6):
                    x_1 = x + (10 * camera.rect.x)
                    y_1 = y + (6 * camera.rect.y)
                    tile = layer.tiles[y_1][x_1]
                    xloc = x * room1.sprite_sheet.tile_width
                    yloc = y * room1.sprite_sheet.tile_height
                    window.window.blit(tile, (xloc, yloc))

        #handles keypresses and moves the player
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_SPACE]:
            player.attack()
        elif pressed[pygame.K_LSHIFT]:
            player.defend()
        elif pressed[pygame.K_LEFT]:
            player.move_west()
        elif pressed[pygame.K_RIGHT]:
            player.move_east()
        elif pressed[pygame.K_UP]:
            player.move_north()
        elif pressed[pygame.K_DOWN]:
            player.move_south()
        else:
            player.make_idle()

        #screen boundaries - the 20s are for handling the spaghetti hitbox #TO-DO
        if player.rect.left > WIN_X * (camera.rect.x + 1) - 20:
            camera.rect.x += 1

        elif player.rect.right < 0 - (WIN_X * abs(camera.rect.x)) + 20:
            camera.rect.x -= 1

        elif player.rect.top > WIN_Y * (camera.rect.y + 1) - 20:
            camera.rect.y += 1

        elif player.rect.bottom < 0 - (WIN_Y * abs(camera.rect.y)) + 20:
            camera.rect.y -= 1

        # draw sprites and update window
        renderer.all_sprites.update()
        renderer.draw()
        update()

if __name__ == "__main__":
    game_loop()
    room1.save()
