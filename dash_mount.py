import math

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

    trapezium = {
        "base": 70.4,
        "top": 92.2,
        "side": 66.8,
    }
    trapezium["top_angle"] = math.degrees(
        math.acos(((trapezium["top"] - trapezium["base"]) / 2) / trapezium["side"])
    )
    angle: float = 180 - (trapezium["top_angle"] * 2)
    offset_for_rotation: float = (
        (trapezium["top"] / (2 * math.cos(math.radians(trapezium["top_angle"]))))
        - trapezium["side"]
        + (lower_plug_d / 2)
    )
    model = right(offset_for_rotation)(plugs_mount)
    model = rotate(angle, UP_VEC)(model)
    model += right(offset_for_rotation)(plugs_mount)
    model = left(offset_for_rotation)(model)

    scad_render_to_file(model, '_%s.scad'% __file__[:-3])

