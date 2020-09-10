import math

from constants import *

class MoveablePoint:
    def __init__(self, x: float = 0, y: float = 0):
        self.x = x
        self.y = y
        self.angle = 0

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

    def set(self, x = 0, y = 0, angle = 0):
        self.x = x
        self.y = y
        self.angle = 0
        return self

    def reset(self):
        return self.set()

    def rotate(self, degrees):
        self.angle += degrees
        self.angle %= 360
        return self

    def forward(self, v):
        self.x += v * math.cos(math.radians(self.angle))
        self.y += v * math.sin(math.radians(self.angle))
        return self

