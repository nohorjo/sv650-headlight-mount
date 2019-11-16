from solid import *
from solid.utils import *

from constants import *

if __name__ == '__main__':
    t: float = 3
    upper_plug_d: float = 7
    lower_plug_d: float = 9.5
    plug_dist: float = 66.8 - ((upper_plug_d + lower_plug_d) / 2)
    plug_h: float = 10

    plug_holes = lambda t: (
        right(plug_dist)(cylinder(h = plug_h, d = upper_plug_d  + (t * 2)))
        + cylinder(h = plug_h, d = lower_plug_d + (t * 2)) 
    )

    plugs_mount = hull()(plug_holes(t)) - plug_holes(0)

    angle: float = 18.78
    offset_for_rotation: float = 215.46 + (lower_plug_d / 2)
    model = right(offset_for_rotation)(plugs_mount)
    model = rotate(angle, UP_VEC)(model)
    model += right(offset_for_rotation)(plugs_mount)
    model = left(offset_for_rotation)(model)

    scad_render_to_file(model, '_%s.scad'% __file__[:-3])

