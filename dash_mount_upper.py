from solid import *
from solid.utils import *

from constants import *
from references import MoveablePoint

lower_plug_d: float = 9.5
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

def dash_mount_upper():
    t: float = 3
    upper_plug_d: float = 7
    plug_h: float = 10

    plug_holes = lambda t: (
        right(trapezium["side"])(cylinder(h = plug_h, d = upper_plug_d  + (t * 2)))
        + cylinder(h = plug_h, d = lower_plug_d + (t * 2)) 
    )

    plugs_mount = hull()(plug_holes(t)) - hole()(plug_holes(0))

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

    factor: float = 0.9
    p = MoveablePoint((trapezium["top"] - trapezium["base"]) / 2)
    mount_point += translate([-(trapezium["top"] * factor) / 2, 0])(
        linear_extrude(10)(
            scale([factor, factor])(polygon([
                p.val(),
                p.right(trapezium["base"]).val(),
                p.up(trapezium["height"])
                    .right((trapezium["top"] - trapezium["base"]) / 2).val(),
                p.left(trapezium["top"]).val(),
            ]))
        )
    )

    return mount_point

if __name__ == '__main__':
    model = dash_mount_upper()

    scad_render_to_file(model, '_%s.scad'% __file__[:-3])

