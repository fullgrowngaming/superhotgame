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

    walk_frames = {0: walk_north, 1: walk_east, 2: walk_south, 3: walk_west}
    def_frames = {0: def_north, 1: def_east, 2: def_south, 3: def_west}
    att_frames = {0: att_north, 1: att_east, 2: att_south, 3: att_west}
    idle_frames = {0: idle, 1: idle, 2: idle, 3: idle}

    all_frames = {State.WALKING: walk_frames, State.DEFENDING: def_frames, State.ATTACKING: att_frames, State.IDLE: idle_frames}

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = (Player.idle[2])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.direction = Directions.SOUTH
        self.state = State.IDLE
        self.anim_timer = 0
        self.attack_cooldown = 0

        self.speed = 1

        self.sword = Sword(self)
        self.shield = Shield(self)

    def update(self):
        #handle attack state and animation
        if self.state == State.ATTACKING:
            if self.anim_timer > 0:
                self.anim_timer -= 1

            #end attack
            else:
                self.speed = 1
                self.state = State.IDLE

        # handle attack cooldown
        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1

        #handle defend state and animation
        if self.state == State.DEFENDING:
            if self.anim_timer > 0:
                self.anim_timer -= 1

        #handle walking state and animations
        if self.state == State.WALKING:
            if self.anim_timer + 1 > 30:
                self.anim_timer = 0

        #handle idle state
        if self.state == State.IDLE:
            self.speed = 1
            self.anim_timer = self.direction.value * 6

        #handle image
        self.image = Player.all_frames[self.state][self.direction.value][self.anim_timer // 6]

    def make_idle(self):
        if not self.state == State.ATTACKING:
            self.state = State.IDLE

    def attack(self):
        if self.state != State.ATTACKING and self.attack_cooldown == 0:
            self.state = State.ATTACKING
            self.speed = 0
            self.attack_cooldown = 30
            self.anim_timer = 17

    def defend(self):
        if self.state != State.ATTACKING and self.state != State.DEFENDING:
            self.state = State.DEFENDING
            self.speed = 0
            self.anim_timer = 12

    def move_north(self):
        if self.state != State.ATTACKING and self.state != State.DEFENDING:
            self.state = State.WALKING
            self.speed = 1
            self.direction = Directions.NORTH
            self.rect.y -= self.speed
            self.anim_timer += 1

    def move_east(self):
        if self.state != State.ATTACKING and self.state != State.DEFENDING:
            self.state = State.WALKING
            self.speed = 1
            self.direction = Directions.EAST
            self.rect.x += self.speed
            self.anim_timer += 1

    def move_south(self):
        if self.state != State.ATTACKING and self.state != State.DEFENDING:
            self.state = State.WALKING
            self.speed = 1
            self.direction = Directions.SOUTH
            self.rect.y += self.speed
            self.anim_timer += 1

    def move_west(self):
        if self.state != State.ATTACKING and self.state != State.DEFENDING:
            self.state = State.WALKING
            self.speed = 1
            self.direction = Directions.WEST
            self.rect.x -= self.speed
            self.anim_timer += 1

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

    sword_walk_frames = {0: walk_north, 1: walk_east, 2: walk_south, 3: walk_west}
    sword_def_frames = {0: def_north, 1: def_east, 2: def_south, 3: def_west}
    sword_att_frames = {0: att_north, 1: att_east, 2: att_south, 3: att_west}
    sword_idle_frames = {0: idle, 1: idle, 2: idle, 3: idle}

    all_sword_frames = {State.WALKING: sword_walk_frames, State.DEFENDING: sword_def_frames,
                        State.ATTACKING: sword_att_frames, State.IDLE: sword_idle_frames}

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

        self.image = Sword.all_sword_frames[self.player.state][self.player.direction.value][self.player.anim_timer // 6]

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

    shield_walk_frames = {0: walk_north, 1: walk_east, 2: walk_south, 3: walk_west}
    shield_def_frames = {0: def_north, 1: def_east, 2: def_south, 3: def_west}
    shield_att_frames = {0: att_north, 1: att_east, 2: att_south, 3: att_west}
    shield_idle_frames = {0: idle, 1: idle, 2: idle, 3: idle}

    all_shield_frames = {State.WALKING: shield_walk_frames, State.DEFENDING: shield_def_frames,
                        State.ATTACKING: shield_att_frames, State.IDLE: shield_idle_frames}

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

        self.image = Shield.all_shield_frames[self.player.state][self.player.direction.value][self.player.anim_timer // 6]


class Effect(pygame.sprite.Sprite):
    att_south = [pygame.image.load('Game/p_attack/Player_Effect_Normal_South_Attack_000%s.png' % frame) for frame in reversed(range(0, 4))]
    att_north = [pygame.image.load('Game/p_attack/Player_Effect_Normal_North_Attack_000%s.png' % frame) for frame in reversed(range(0, 4))]
    att_east = [pygame.image.load('Game/p_attack/Player_Effect_Normal_East_Attack_000%s.png' % frame) for frame in reversed(range(0, 4))]
    att_west = [pygame.image.load('Game/p_attack/Player_Effect_Normal_West_Attack_000%s.png' % frame) for frame in reversed(range(0, 4))]

    effect_att_frames = {0: att_north, 1: att_east, 2: att_south, 3: att_west}

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
            self.image = Effect.effect_att_frames[self.player.direction.value][self.player.anim_timer // 6]
        else:
            self.image = test











