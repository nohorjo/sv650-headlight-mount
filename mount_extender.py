from solid import *
from solid.utils import *

from constants import *

mh: float = 2.5

def mount_part():
    model = circle(d = 26)
    model += forward(13)(square([30, 1], True))
    model = hull()(model)
    model = linear_extrude(mh)(model)

    return model

if __name__ == '__main__':
    holes = circle(d = 9)
    holes += back(20)(circle(d = 9))

    model = hull()(holes + forward(7)(square([24, 1], True)))
    model = minkowski()(circle(r = 6), model)
    model -= holes

    h: float = 8
    model = linear_extrude(h)(model)

    model -= up((h - mh)/ 2)(mount_part())

    scad_render_to_file(model, '_%s.scad'% __file__[:-3])

