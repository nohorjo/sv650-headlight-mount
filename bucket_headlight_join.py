from solid import *
from solid.utils import *

from constants import *
from super_hole import *
from references import *
from chamfer import *

if __name__ == '__main__':
    outer_r: float = 83
    thick: float = 3
    base_h: float = thick + 3
    model = circle(r = outer_r + thick)
    model -= circle(r = outer_r - (thick * 2))
    model = linear_extrude(base_h)(model)

    gap = circle(r = outer_r)
    gap -= circle(r = outer_r - thick)
    gap = linear_extrude(thick)(gap)
    model -= gap

    tab_r: float = 71.6
    tab_x: float = 11
    tab_y: float = 2.5
    tab = cube([tab_x, tab_y, 8], True)
    tab = up(8 / 2)(tab)
    tab += translate([-tab_x / 2, tab_y / 2, 1])(chamfer(tab_x, 3))
    tab = translate([0, tab_r, base_h])(tab)

    for i in range(3):
        model += rotate(120 * i, UP_VEC)(tab)

    tab_base = circle(r = outer_r)
    tab_base -= circle(r = tab_r)
    tab_base = linear_extrude(thick / 2)(tab_base)
    tab_base = up(base_h)(tab_base)

    model += tab_base

    scad_render_to_file(model, '_%s.scad'% __file__[:-3])

