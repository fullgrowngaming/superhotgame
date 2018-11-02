import pygame, time, sys, random
from GameWindow import GameWindow
from Player import Player
from Renderer import Renderer

pygame.init()
player = Player(50,50)
window = GameWindow(240, 135)
clock = pygame.time.Clock()
renderer = Renderer()
renderer.sprites_list.add(player)

def update():
    window.display()
    clock.tick(60)
    print(f'x, y: {player.x},{player.y} | Direction: {player.direction}')

def game_loop():
    running = True
    while running:
        window.window.fill(GameWindow.white)

        #handle quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        #handles keypresses and moves the player
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]:
            player.move(3)
        elif pressed[pygame.K_RIGHT]:
            player.move(1)
        elif pressed[pygame.K_UP]:
            player.move(0)
        elif pressed[pygame.K_DOWN]:
            player.move(2)
        else:
            player.move(4)  #if you stop moving (i.e. not holding a direction)
            player.walk_count = 0 #reset walking animation

        #draw sprites and update window
        renderer.draw(window)
        update()

if __name__ == "__main__":
    game_loop()

