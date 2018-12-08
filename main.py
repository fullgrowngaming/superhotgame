import pygame, time, sys, random
from GameWindow import GameWindow
from Player import *
from Editor.Room import Room
from Renderer import Renderer
from Camera import Camera
from Level import Level, LevelOverlay
from Pillar import Pillar
import json
pygame.init()

WIN_X, WIN_Y = 384,216

#OBJECTS
window = GameWindow(WIN_X, WIN_Y)
pillar = Pillar()
camera = Camera(WIN_X, WIN_Y)
level = Level(); level_overlay = LevelOverlay()
player = Player(125,60)
effect = Effect(player)
clock = pygame.time.Clock()
renderer = Renderer(camera, window)

renderer.all_sprites.add(player, player.sword, player.shield, effect, pillar)

def update():
    window.display()
    clock.tick(60)
    print(f'Camera X,Y: {camera.rect.x},{camera.rect.y} | Player X,Y: {player.rect.x},{player.rect.y}'
          f' State: {player.state}, Speed: {player.speed}, Anim Timer: {player.anim_timer}'
          f' Camera State: {camera.state}')

def game_loop():
    running = True
    while running:
        #handle quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        #draw background
        window.window.blit(level.image, (0,0))

        #handles keypresses and moves the player
        pressed = pygame.key.get_pressed()
        if not pygame.sprite.collide_mask(player, level):
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
        else:
            player.null_move()

        #screen boundaries - the 20s are for handling the spaghetti hitbox #TO-DO
        if player.rect.left > WIN_X * (camera.rect.x + 1) - 20:
            camera.move_right()

        elif player.rect.right < 0 - (WIN_X * abs(camera.rect.x)) + 20:
            camera.move_left()

        elif player.rect.top > WIN_Y * (camera.rect.y + 1) - 20:
            camera.move_down()

        elif player.rect.bottom < 0 - (WIN_Y * abs(camera.rect.y)) + 20:
            camera.move_up()

        # draw sprites and update window
        renderer.all_sprites.update()
        camera.update()
        renderer.draw()
        window.window.blit(level_overlay.image, (0, 0))
        update()

if __name__ == "__main__":
    game_loop()
    room1.save()
