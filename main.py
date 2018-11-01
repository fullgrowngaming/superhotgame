import pygame, time, sys, random
from GameWindow import GameWindow
from Player import Player

pygame.init()
player = Player(50,50)
window = GameWindow(240, 135)
clock = pygame.time.Clock()
test = pygame.sprite.Group()
test.add(player)

def update():
    window.display()
    clock.tick(60)

def game_loop():
    running = True
    while running:
        window.window.fill(GameWindow.white)
        print (test.sprites())
        #handle quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        #handles keypresses and moves the player
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]:
            player.previous_direction = player.direction
            player.direction = 3
        elif pressed[pygame.K_RIGHT]:
            player.previous_direction = player.direction
            player.direction = 1
        elif pressed[pygame.K_UP]:
            player.previous_direction = player.direction
            player.direction = 0
        elif pressed[pygame.K_DOWN]:
            player.previous_direction = player.direction
            player.direction = 2
        elif player.direction != 4:
                player.previous_direction = player.direction
                player.direction = 4 #set to idle
                player.walk_count = 0 #reset walking animation

        player.move()

        # update screen and tick
        player.draw(window)
        update()

if __name__ == "__main__":
    game_loop()

