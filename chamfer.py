import math

from solid import *
from solid.utils import *

def chamfer(x, y):
    model = cube([x, y, y])
    diag = math.sqrt(y**2 + y**2)
    model -= forward(y)(rotate(45, RIGHT_VEC)(cube([x, diag, diag])))

    return model
