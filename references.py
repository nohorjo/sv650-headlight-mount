from solid import *
from solid.utils import *

from constants import *

class MoveablePoint:
    def __init__(self, x: float = 0, y: float = 0):
        self.x = x
        self.y = y

    def val(self):
        return [self.x, self.y]

    def up(self, v: float):
        self.y += v
        return self

    def down(self, v: float):
        self.y -= v
        return self

    def left(self, v: float):
        self.x -= v
        return self

    def right(self, v: float):
        self.x += v
        return self

