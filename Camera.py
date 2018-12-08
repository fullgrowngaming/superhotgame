import pygame
from enum import Enum

class State(Enum):
    UP = 0
    LEFT = 1
    DOWN = 2
    RIGHT = 3
    IDLE = 4

class Camera():
    OFFSET = (1/60)
    def __init__(self, width, height):
        self.rect = pygame.Rect(0,0, width, height)
        self.state = State.IDLE
        self.xtimer = 0
        self.ytimer = 0

    def update(self):
        if self.xtimer == 0 and self.ytimer == 0:
            self.state = State.IDLE

        elif self.state == State.UP:
            self.ytimer -= 1

        elif self.state == State.RIGHT:
            self.xtimer -= 1

        elif self.state == State.DOWN:
            self.ytimer -= 1

        elif self.state == State.LEFT:
            self.xtimer -= 1

    def move_up(self):
        if self.state == State.IDLE:
            self.state = State.UP
            self.ytimer = 60
            self.rect.y -= 1

    def move_right(self):
        if self.state == State.IDLE:
            self.state = State.RIGHT
            self.xtimer = 30
            self.rect.x += 1

    def move_down(self):
        if self.state == State.IDLE:
            self.state = State.DOWN
            self.ytimer = 60
            self.rect.y += 1

    def move_left(self):
        if self.state == State.IDLE:
            self.state = State.LEFT
            self.xtimer = 60
            self.rect.x -= 1

