import pygame
from GameWindow import GameWindow

class Player(pygame.sprite.Sprite):
    walk_south = [pygame.image.load('Game/p_run/Player_South_Run_000%s.png' % frame) for frame in range(1, 6)]
    walk_north = [pygame.image.load('Game/p_run/Player_North_Run_000%s.png' % frame) for frame in range(1, 6)]
    walk_east = [pygame.image.load('Game/p_run/Player_East_Run_000%s.png' % frame) for frame in range(1, 6)]
    walk_west = [pygame.image.load('Game/p_run/Player_West_Run_000%s.png' % frame) for frame in range(1, 6)]
    idle = [pygame.image.load('Game/p_idle/idle_%s.png' % direction) for direction in 'nesw']

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x, self.y = x, y
        self.width, self.height = 48, 48
        self.walk_count = 0
        #self.previous_direction = 1
        self.direction = 2
        self.speed = 1

    def add(self):
        pygame.sprite.Group.add(self)

    def move(self, direction):
        if direction == 2:
            self.direction = 2
            self.y += self.speed

        if direction == 0:
            self.direction = 0
            self.y -= self.speed

        if direction == 1:
            self.direction = 1
            self.x += self.speed

        if direction == 3:
            self.direction = 3
            self.x -= self.speed

    def draw(self, GameWindow):
        if self.walk_count + 1 >= 30:
            self.walk_count = 0

        if self.direction == 0:
            GameWindow.draw(Player.walk_north[self.walk_count // 6], (self.x, self.y))
            self.walk_count += 1

        elif self.direction == 1:
            GameWindow.draw(Player.walk_east[self.walk_count // 6], (self.x, self.y))
            self.walk_count += 1

        elif self.direction == 2:
            GameWindow.draw(Player.walk_south[self.walk_count // 6], (self.x, self.y))
            self.walk_count += 1

        elif self.direction == 3:
            GameWindow.draw(Player.walk_west[self.walk_count // 6], (self.x, self.y))
            self.walk_count += 1





