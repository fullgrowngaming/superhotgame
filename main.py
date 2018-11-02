import pygame, time, sys, random
from GameWindow import GameWindow
from Player import Player

pygame.init()
player = Player(50,50)
window = GameWindow(240, 135)
clock = pygame.time.Clock()

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
        else:                     #if you aren't holding anything, i.e. if you aren't moving anymore
            player.walk_count = 0 #reset walking animation

        #update screen and tick
        player.draw(window)
        update()

if __name__ == "__main__":
    game_loop()

