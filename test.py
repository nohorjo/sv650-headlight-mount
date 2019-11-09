from functools import reduce
from solid import *
from solid.utils import *

from constants import *
from super_hole import *
from references import *


if __name__ == '__main__':
    outer_r: float = 83
    thick: float = 2
    model = circle(r = outer_r + thick)
    model -= circle(r = outer_r - (thick * 2))
    model = linear_extrude(5)(model)

    gap = circle(r = outer_r)
    gap -= circle(r = outer_r - thick)
    gap = linear_extrude(5 - thick)(gap)

    tab = translate([0, 71.6, 8 / 2])(cube([11, 2.5, 8], True))

    model -= gap
    for i in range(3):
        model += rotate(120 * i, UP_VEC)(tab)

    scad_render_to_file(model, '_%s.scad'% __file__[:-3])

