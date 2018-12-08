from enum import Enum

class Direction(Enum):
    TEST = 0
    WHAT = 1

direction = Direction.TEST

print(direction)
print(direction.value)