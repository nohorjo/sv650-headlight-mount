import math

from solid import *
from solid.utils import *

from constants import *
from references import bucket, MoveablePoint

if __name__ == '__main__':
    t: float = 3
    upper_plug_d: float = 7
    lower_plug_d: float = 9.5
    plug_dist: float = 66.8 - ((upper_plug_d + lower_plug_d) / 2)
    plug_h: float = 10
    tilt_angle: float = 60
    rise: float = 100

    plug_holes = lambda t: (
        right(plug_dist)(cylinder(h = plug_h, d = upper_plug_d  + (t * 2)))
        + cylinder(h = plug_h, d = lower_plug_d + (t * 2)) 
    )

    plugs_mount = hull()(plug_holes(t)) - hole()(plug_holes(0))

    trapezium = {
        "base": 70.4,
        "top": 92.2,
        "side": 66.8,
    }
    trapezium["top_angle"] = math.degrees(
        math.acos(
            ((trapezium["top"] - trapezium["base"]) / 2)
            / trapezium["side"]
        )
    )
    trapezium["height"] = math.sin(math.radians(trapezium["top_angle"])) * trapezium["side"]
    trapezium["sides_angle"] = 180 - (trapezium["top_angle"] * 2)
    offset_for_rotation: float = (
        (trapezium["top"] / (2 * math.cos(math.radians(trapezium["top_angle"]))))
        - trapezium["side"]
        + (lower_plug_d / 2)
    )


    mount_point = right(offset_for_rotation)(plugs_mount)
    mount_point = rotate(trapezium["sides_angle"], UP_VEC)(mount_point)
    mount_point += right(offset_for_rotation)(plugs_mount)
    mount_point = left(offset_for_rotation)(mount_point)

    mount_point = rotate(90 - (trapezium["sides_angle"] / 2), UP_VEC)(mount_point)
    mount_point = right(trapezium["base"] / 2)(mount_point)
    mount_point = rotate(tilt_angle, RIGHT_VEC)(mount_point)
    mount_point = up(rise)(mount_point)


    p = MoveablePoint((trapezium["top"] - trapezium["base"]) / 2)

    x: float = 175
    base = cylinder(h = x, d = 35) - hole()(cylinder(h = x, d = 10))
    base = rotate(90, FORWARD_VEC)(base)
    base = translate([-x / 2, 40 + (35 / 2)])(base)

    factor: float = 0.8
    base += translate([-(trapezium["top"] * factor) / 2, 0, rise])(
        rotate(tilt_angle, RIGHT_VEC)(
            linear_extrude(10)(
                scale([factor, factor])(polygon([
                    p.val(),
                    p.right(trapezium["base"]).val(),
                    p.up(trapezium["height"]).right((trapezium["top"] - trapezium["base"]) / 2).val(),
                    p.left(trapezium["top"]).val(),
                ]))
            )
        )
    )

    base = hull()(base)

    base -= translate([-30, -10, rise - 20])(cube([60, 100, 100]))

    model = mount_point + base

    factor = 1.05
    model += forward(100)(rotate(90, RIGHT_VEC)(bucket()))
    model -= forward(100)(scale([factor, factor, factor])(rotate(90, RIGHT_VEC)(bucket(False))))


    scad_render_to_file(model, '_%s.scad'% __file__[:-3])

