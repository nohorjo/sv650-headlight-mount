from solid import *
from solid.utils import *

from constants import *
from super_hole import *
from references import *
from chamfer import *

if __name__ == '__main__':
    outer_r: float = 86 # 85 86 88 90 83
    thick: float = 3
    base_h: float = thick + 3
    model = circle(r = outer_r + thick)
    model -= circle(r = outer_r - (thick * 2))
    model = linear_extrude(base_h)(model)

    gap = circle(r = outer_r)
    gap -= circle(r = outer_r - thick)
    gap = linear_extrude(thick)(gap)
    model -= gap

    tab_r: float = 82
    tab_x: float = 10
    tab_y: float = 2
    tab_z: float = 8
    tab = cube([tab_x, tab_y, tab_z], True)
    tab = up(tab_z / 2)(tab)
    tab += left(tab_x / 2)(cube([tab_x, 7, thick]))
    tab += translate([-tab_x / 2, tab_y / 2, 1])(
        chamfer(tab_x, 3)
        + translate([0, 3, -1])(rotate(180, RIGHT_VEC)(chamfer(tab_x, 2)))
    )
    tab = translate([0, tab_r, base_h])(tab)

    model += tab
    model += rotate(130, DOWN_VEC)(tab)
    model += rotate(230, DOWN_VEC)(tab)

    scad_render_to_file(model, '_%s.scad'% __file__[:-3])

