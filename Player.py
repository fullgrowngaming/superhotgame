import pygame
from enum import Enum

test = pygame.image.load('Game/test.png')

class Directions(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

class State(Enum):
    ATTACKING = 0
    DEFENDING = 1
    WALKING = 2
    IDLE = 3

class Player(pygame.sprite.Sprite):
    idle = [pygame.image.load('Game/p_idle/idle_%s.png' % direction) for direction in 'nesw']

    walk_south = [pygame.image.load('Game/p_run_2/Player_South_Run_000%s.png' % frame) for frame in range(0, 6)]
    walk_north = [pygame.image.load('Game/p_run_2/Player_North_Run_000%s.png' % frame) for frame in range(0, 6)]
    walk_east = [pygame.image.load('Game/p_run_2/Player_East_Run_000%s.png' % frame) for frame in range(0, 6)]
    walk_west = [pygame.image.load('Game/p_run_2/Player_West_Run_000%s.png' % frame) for frame in range(0, 6)]

    att_south = [pygame.image.load('Game/p_attack/Player_South_Attack_000%s.png' % frame) for frame in reversed(range(0,4))]
    att_north = [pygame.image.load('Game/p_attack/Player_North_Attack_000%s.png' % frame) for frame in reversed(range(0,4))]
    att_east = [pygame.image.load('Game/p_attack/Player_East_Attack_000%s.png' % frame) for frame in reversed(range(0,4))]
    att_west = [pygame.image.load('Game/p_attack/Player_West_Attack_000%s.png' % frame) for frame in reversed(range(0,4))]

    def_south = [pygame.image.load('Game/p_defend/Player_South_Defend_000%s.png' % frame) for frame in reversed(range(0,2))]
    def_north = [pygame.image.load('Game/p_defend/Player_North_Defend_000%s.png' % frame) for frame in reversed(range(0,2))]
    def_east = [pygame.image.load('Game/p_defend/Player_East_Defend_000%s.png' % frame) for frame in reversed(range(0,2))]
    def_west = [pygame.image.load('Game/p_defend/Player_West_Defend_000%s.png' % frame) for frame in reversed(range(0,2))]

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = (Player.idle[2])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.walk_count = 0
        self.direction = Directions.SOUTH
        self.state = State.IDLE

        self.attack_anim_timer = 0
        self.attack_cooldown = 0
        self.defend_anim_timer = 0

        self.speed = 1

        self.sword = Sword(self)
        self.shield = Shield(self)

    def update(self):
        #handle attack state and animation
        if self.state == State.ATTACKING:
            if self.attack_anim_timer > 0:
                self.attack_anim_timer -= 1
                if self.direction == Directions.NORTH:
                    self.image = (Player.att_north[self.attack_anim_timer // 6])
                if self.direction == Directions.EAST:
                    self.image = (Player.att_east[self.attack_anim_timer // 6])
                if self.direction == Directions.SOUTH:
                    self.image = (Player.att_south[self.attack_anim_timer // 6])
                if self.direction == Directions.WEST:
                    self.image = (Player.att_west[self.attack_anim_timer // 6])

            #end attack
            else:
                self.speed = 1
                self.state = State.IDLE

        # handle attack cooldown
        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1

        #handle defend state and animation
        if self.state == State.DEFENDING:
            if self.defend_anim_timer > 0:
                self.defend_anim_timer -= 1
                if self.direction == Directions.NORTH:
                    self.image = (Player.def_north[self.defend_anim_timer // 6])
                if self.direction == Directions.EAST:
                    self.image = (Player.def_east[self.defend_anim_timer // 6])
                if self.direction == Directions.SOUTH:
                    self.image = (Player.def_south[self.defend_anim_timer // 6])
                if self.direction == Directions.WEST:
                    self.image = (Player.def_west[self.defend_anim_timer // 6])

        #handle walking state and animations
        if self.state == State.WALKING:
            if self.walk_count + 1 > 30:
                self.walk_count = 0
            if self.direction == Directions.NORTH:
                self.image = (Player.walk_north[self.walk_count // 6])
            if self.direction == Directions.EAST:
                self.image = (Player.walk_east[self.walk_count // 6])
            if self.direction == Directions.SOUTH:
                self.image = (Player.walk_south[self.walk_count // 6])
            if self.direction == Directions.WEST:
                self.image = (Player.walk_west[self.walk_count // 6])

        #handle idle state
        if self.state == State.IDLE:
            self.speed = 1
            self.image = (Player.idle[self.direction.value])
            self.walk_count = 0

    def make_idle(self):
        if not self.state == State.ATTACKING:
            self.state = State.IDLE

    def attack(self):
        if self.state != State.ATTACKING and self.attack_cooldown == 0:
            self.state = State.ATTACKING
            self.speed = 0
            self.attack_cooldown = 30
            self.attack_anim_timer = 17

    def defend(self):
        if self.state != State.ATTACKING and self.state != State.DEFENDING:
            self.state = State.DEFENDING
            self.speed = 0
            self.defend_anim_timer = 12

    def move_north(self):
        if self.state != State.ATTACKING and self.state != State.DEFENDING:
            self.state = State.WALKING
            self.speed = 1
            self.direction = Directions.NORTH
            self.rect.y -= self.speed
            self.walk_count += 1

    def move_east(self):
        if self.state != State.ATTACKING and self.state != State.DEFENDING:
            self.state = State.WALKING
            self.speed = 1
            self.direction = Directions.EAST
            self.rect.x += self.speed
            self.walk_count += 1

    def move_south(self):
        if self.state != State.ATTACKING and self.state != State.DEFENDING:
            self.state = State.WALKING
            self.speed = 1
            self.direction = Directions.SOUTH
            self.rect.y += self.speed
            self.walk_count += 1

    def move_west(self):
        if self.state != State.ATTACKING and self.state != State.DEFENDING:
            self.state = State.WALKING
            self.speed = 1
            self.direction = Directions.WEST
            self.rect.x -= self.speed
            self.walk_count += 1

class Sword(pygame.sprite.Sprite):
    idle = [pygame.image.load('Game/p_idle/Player_Sword_Normal_%s_Idle_0000.png' % direction) for direction in 'nesw']

    walk_south = [pygame.image.load('Game/p_run_2/Player_Sword_Normal_South_Run_000%s.png' % frame) for frame in range(0, 6)]
    walk_north = [pygame.image.load('Game/p_run_2/Player_Sword_Normal_North_Run_000%s.png' % frame) for frame in range(0, 6)]
    walk_east = [pygame.image.load('Game/p_run_2/Player_Sword_Normal_East_Run_000%s.png' % frame) for frame in range(0, 6)]
    walk_west = [pygame.image.load('Game/p_run_2/Player_Sword_Normal_West_Run_000%s.png' % frame) for frame in range(0, 6)]

    att_south = [pygame.image.load('Game/p_attack/Player_Sword_Normal_South_Attack_000%s.png' % frame) for frame in reversed(range(0,4))]
    att_north = [pygame.image.load('Game/p_attack/Player_Sword_Normal_North_Attack_000%s.png' % frame) for frame in reversed(range(0,4))]
    att_east = [pygame.image.load('Game/p_attack/Player_Sword_Normal_East_Attack_000%s.png' % frame) for frame in reversed(range(0,4))]
    att_west = [pygame.image.load('Game/p_attack/Player_Sword_Normal_West_Attack_000%s.png' % frame) for frame in reversed(range(0,4))]

    def_south = [pygame.image.load('Game/p_defend/Player_Sword_Normal_South_Defend_000%s.png' % frame) for frame in range(0, 2)]
    def_north = [pygame.image.load('Game/p_defend/Player_Sword_Normal_North_Defend_000%s.png' % frame) for frame in range(0, 2)]
    def_east = [pygame.image.load('Game/p_defend/Player_Sword_Normal_East_Defend_000%s.png' % frame) for frame in range(0, 2)]
    def_west = [pygame.image.load('Game/p_defend/Player_Sword_Normal_West_Defend_000%s.png' % frame) for frame in range(0, 2)]

    def __init__(self, Player):
        pygame.sprite.Sprite.__init__(self)
        self.image = self.walk_south[0]
        self.rect = self.image.get_rect()
        self.player = Player
        self.rect.x = Player.rect.x
        self.rect.y = Player.rect.y

    def update(self):
        self.rect.x = self.player.rect.x
        self.rect.y = self.player.rect.y

        if self.player.state == State.ATTACKING:
            if self.player.direction == Directions.NORTH:
                self.image = (Sword.att_north[self.player.attack_anim_timer // 6])
            elif self.player.direction == Directions.EAST:
                self.image = (Sword.att_east[self.player.attack_anim_timer // 6])
            elif self.player.direction == Directions.SOUTH:
                self.image = (Sword.att_south[self.player.attack_anim_timer // 6])
            elif self.player.direction == Directions.WEST:
                self.image = (Sword.att_west[self.player.attack_anim_timer // 6])

        elif self.player.state == State.WALKING:
            if self.player.direction == Directions.NORTH:
                self.image = (Sword.walk_north[self.player.walk_count // 6])
            elif self.player.direction == Directions.EAST:
                self.image = (Sword.walk_east[self.player.walk_count // 6])
            elif self.player.direction == Directions.SOUTH:
                self.image = (Sword.walk_south[self.player.walk_count // 6])
            elif self.player.direction == Directions.WEST:
                self.image = (Sword.walk_west[self.player.walk_count // 6])

        elif self.player.state == State.DEFENDING:
            if self.player.direction == Directions.NORTH:
                self.image = (Sword.def_north[self.player.defend_anim_timer // 6])
            elif self.player.direction == Directions.EAST:
                self.image = (Sword.def_east[self.player.defend_anim_timer // 6])
            elif self.player.direction == Directions.SOUTH:
                self.image = (Sword.def_south[self.player.defend_anim_timer // 6])
            elif self.player.direction == Directions.WEST:
                self.image = (Sword.def_west[self.player.defend_anim_timer // 6])

        elif self.player.state == State.IDLE:
            self.image = Sword.idle[self.player.direction.value]


class Shield(pygame.sprite.Sprite):
    idle = [pygame.image.load('Game/p_idle/Player_Shield_Normal_%s_Idle_0000.png' % direction) for direction in 'nesw']

    walk_south = [pygame.image.load('Game/p_run_2/Player_Shield_Normal_South_Run_000%s.png' % frame) for frame in range(0, 6)]
    walk_north = [pygame.image.load('Game/p_run_2/Player_Shield_Normal_North_Run_000%s.png' % frame) for frame in range(0, 6)]
    walk_east = [pygame.image.load('Game/p_run_2/Player_Shield_Normal_East_Run_000%s.png' % frame) for frame in range(0, 6)]
    walk_west = [pygame.image.load('Game/p_run_2/Player_Shield_Normal_West_Run_000%s.png' % frame) for frame in range(0, 6)]

    att_south = [pygame.image.load('Game/p_attack/Player_Shield_Normal_South_Attack_000%s.png' % frame) for frame in reversed(range(0, 4))]
    att_north = [pygame.image.load('Game/p_attack/Player_Shield_Normal_North_Attack_000%s.png' % frame) for frame in reversed(range(0, 4))]
    att_east = [pygame.image.load('Game/p_attack/Player_Shield_Normal_East_Attack_000%s.png' % frame) for frame in reversed(range(0, 4))]
    att_west = [pygame.image.load('Game/p_attack/Player_Shield_Normal_West_Attack_000%s.png' % frame) for frame in reversed(range(0, 4))]

    def_south = [pygame.image.load('Game/p_defend/Player_Shield_Normal_South_Defend_000%s.png' % frame) for frame in range(0, 2)]
    def_north = [pygame.image.load('Game/p_defend/Player_Shield_Normal_North_Defend_000%s.png' % frame) for frame in range(0, 2)]
    def_east = [pygame.image.load('Game/p_defend/Player_Shield_Normal_East_Defend_000%s.png' % frame) for frame in range(0, 2)]
    def_west = [pygame.image.load('Game/p_defend/Player_Shield_Normal_West_Defend_000%s.png' % frame) for frame in range(0, 2)]

    def __init__(self, Player):
        pygame.sprite.Sprite.__init__(self)
        self.image = self.walk_south[0]
        self.rect = self.image.get_rect()
        self.player = Player
        self.rect.x = Player.rect.x
        self.rect.y = Player.rect.y

    def update(self):
        self.rect.x = self.player.rect.x
        self.rect.y = self.player.rect.y

        if self.player.state == State.ATTACKING:
            if self.player.direction == Directions.NORTH:
                self.image = (Shield.att_north[self.player.attack_anim_timer // 6])
            elif self.player.direction == Directions.EAST:
                self.image = (Shield.att_east[self.player.attack_anim_timer // 6])
            elif self.player.direction == Directions.SOUTH:
                self.image = (Shield.att_south[self.player.attack_anim_timer // 6])
            elif self.player.direction == Directions.WEST:
                self.image = (Shield.att_west[self.player.attack_anim_timer // 6])

        elif self.player.state == State.WALKING:
            if self.player.direction == Directions.NORTH:
                self.image = (Shield.walk_north[self.player.walk_count // 6])
            elif self.player.direction == Directions.EAST:
                self.image = (Shield.walk_east[self.player.walk_count // 6])
            elif self.player.direction == Directions.SOUTH:
                 self.image = (Shield.walk_south[self.player.walk_count // 6])
            elif self.player.direction == Directions.WEST:
                self.image = (Shield.walk_west[self.player.walk_count // 6])

        elif self.player.state == State.DEFENDING:
            if self.player.direction == Directions.NORTH:
                self.image = (Shield.def_north[self.player.defend_anim_timer // 6])
            elif self.player.direction == Directions.EAST:
                self.image = (Shield.def_east[self.player.defend_anim_timer // 6])
            elif self.player.direction == Directions.SOUTH:
                self.image = (Shield.def_south[self.player.defend_anim_timer // 6])
            elif self.player.direction == Directions.WEST:
                self.image = (Shield.def_west[self.player.defend_anim_timer // 6])

        elif self.player.state == State.IDLE:
            self.image = Shield.idle[self.player.direction.value]


class Effect(pygame.sprite.Sprite):
    att_south = [pygame.image.load('Game/p_attack/Player_Effect_Normal_South_Attack_000%s.png' % frame) for frame in reversed(range(0, 4))]
    att_north = [pygame.image.load('Game/p_attack/Player_Effect_Normal_North_Attack_000%s.png' % frame) for frame in reversed(range(0, 4))]
    att_east = [pygame.image.load('Game/p_attack/Player_Effect_Normal_East_Attack_000%s.png' % frame) for frame in reversed(range(0, 4))]
    att_west = [pygame.image.load('Game/p_attack/Player_Effect_Normal_West_Attack_000%s.png' % frame) for frame in reversed(range(0, 4))]

    def __init__(self, Player):
        pygame.sprite.Sprite.__init__(self)
        self.image = self.att_north[0]
        self.rect = self.image.get_rect()
        self.player = Player
        self.rect.x = Player.rect.x
        self.rect.y = Player.rect.y

    def update(self):
        self.rect.x = self.player.rect.x
        self.rect.y = self.player.rect.y

        if self.player.state == State.ATTACKING:
            if self.player.direction == Directions.NORTH:
                self.image = (Effect.att_north[self.player.attack_anim_timer // 6])
            elif self.player.direction == Directions.EAST:
                self.image = (Effect.att_east[self.player.attack_anim_timer // 6])
            elif self.player.direction == Directions.SOUTH:
                self.image = (Effect.att_south[self.player.attack_anim_timer // 6])
            elif self.player.direction == Directions.WEST:
                self.image = (Effect.att_west[self.player.attack_anim_timer // 6])
        else:
            self.image = test











