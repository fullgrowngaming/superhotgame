import pygame
from GameWindow import GameWindow

class Player(pygame.sprite.Sprite):
    walk_south = [pygame.image.load('Game/p_run/Player_South_Run_000%s.png' % frame) for frame in range(1, 6)]
    walk_north = [pygame.image.load('Game/p_run/Player_North_Run_000%s.png' % frame) for frame in range(1, 6)]
    walk_east = [pygame.image.load('Game/p_run/Player_East_Run_000%s.png' % frame) for frame in range(1, 6)]
    walk_west = [pygame.image.load('Game/p_run/Player_West_Run_000%s.png' % frame) for frame in range(1, 6)]
    idle = [pygame.image.load('Game/p_idle/idle_%s.png' % direction) for direction in 'nesw']

    att_south = [pygame.image.load('Game/p_attack/Player_South_Attack_000%s.png' % frame) for frame in range(1, 4)]
    att_north = [pygame.image.load('Game/p_attack/Player_North_Attack_000%s.png' % frame) for frame in range(1, 4)]
    att_east = [pygame.image.load('Game/p_attack/Player_East_Attack_000%s.png' % frame) for frame in range(1, 4)]
    att_west = [pygame.image.load('Game/p_attack/Player_West_Attack_000%s.png' % frame) for frame in range(1, 4)]

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x, self.y = x, y
        self.width, self.height = 48, 48

        self.image = (Player.idle[1])
        self.rect = self.image.get_rect()
        self.rect.center = (self.width / 2, self.height / 2)

        self.walk_count = 0

        self.attack_anim_timer = 0
        self.attack_cooldown = 0

        self.direction = 2
        self.walking = False

        self.speed = 1

    def update(self):
        self.attack_anim_timer -= 1

        if self.attack_anim_timer > 0:
            if self.direction == 0:
                self.image = (Player.att_north[self.attack_anim_timer // 6])
            if self.direction == 1:
                self.image = (Player.att_east[self.attack_anim_timer // 6])
            if self.direction == 2:
                self.image = (Player.att_south[self.attack_anim_timer // 6])
            if self.direction == 3:
                self.image = (Player.att_west[self.attack_anim_timer // 6])

        elif self.attack_anim_timer == 0:
            self.speed = 1

        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1


    def attack(self):
        print('attack')
        self.speed = 0
        self.attack_cooldown = 60
        self.attack_anim_timer = 17

    def move(self, direction):
        self.walking = True
        if self.walk_count + 1 >= 30:
            self.walk_count = 0

        if direction == 0:
            self.direction = 0
            self.y -= self.speed
            self.image = (Player.walk_north[self.walk_count // 6])
            self.walk_count += 1

        if direction == 1:
            self.direction = 1
            self.x += self.speed
            self.image = (Player.walk_east[self.walk_count // 6])
            self.walk_count += 1

        if direction == 2:
            self.direction = 2
            self.y += self.speed
            self.image = (Player.walk_south[self.walk_count // 6])
            self.walk_count += 1

        if direction == 3:
            self.direction = 3
            self.x -= self.speed
            self.image = (Player.walk_west[self.walk_count // 6])
            self.walk_count += 1

        if direction == 4:
            self.image = (Player.idle[self.direction])
            self.walk_count = 0
            self.walking = False










