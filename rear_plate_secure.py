from solid import *
from solid.utils import *

from constants import *

def rear_plate_secure():
    x: float = 50
    z: float = 15
    model = cube([x, rear_join_y, z])
    model -= translate([0, rear_join_y / 2, 3.5])(rotate(90, FORWARD_VEC)(cylinder(h = x, d = screw_d)))

    return model

if __name__ == '__main__':
    model = rear_plate_secure()

    scad_render_to_file(model, '_%s.scad'% __file__[:-3])

