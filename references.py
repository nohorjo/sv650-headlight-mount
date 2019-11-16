from solid import *
from solid.utils import *

from constants import *
from super_hole import *

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

def fork():
    model = cylinder(h = 200, d = fork_d)
    model = right(fork_dist)(model)
    model += cylinder(h = 200, d = fork_d)
    model = background(model)
    
    return model

def indicator_hole(_debug = False):
    model = cube([10, 26, 5])

    if _debug:
        return debug(model)
    else:
        return super_hole(model, 'indicator_hole')

def bucket():
    p = MoveablePoint()
    model = polygon([
        p.val(),
        p.up(35.4 + 40).val(),
        p.right(86 / 2).val(),
        p.down(16).val(),
        p.down(40 - 16 + 35.4).right(35.4).val(),
    ])
    
    model = rotate_extrude()(model)
    h: float = 86 + (35.4) * 2
    model += translate([-h / 2, 0, 35.4 / 2])(rotate(90, FORWARD_VEC)(cylinder(h = h, d = 35.4)))

    model = up(25)(model)
    model += cylinder(h = 25, d = h)

    return background(model)

if __name__ == '__main__':
    model = bucket()
    scad_render_to_file(model, '_%s.scad'% __file__[:-3])

