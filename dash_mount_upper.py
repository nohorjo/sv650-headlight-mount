from solid import *
from solid.utils import *

from constants import *
from references import MoveablePoint

lower_plug_d: float = 10.5
trapezium = {
    "base": 59.5,
    "top": 83.5,
    "side": 59,
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
    upper_plug_d: float = 8
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

    
    holes = cylinder(h = dash_link_gap, d = screw_d)
    for i in range(dash_screw_hole_count):
        holes += right(i * (dash_link_base_x / dash_screw_hole_count))(
            hole()(cylinder(h = dash_link_gap, d = screw_d))
        )

    screw_point = cube([30, 17, dash_link_gap - 1])
    screw_point -= translate([10 / 2, 20 / 2])(holes)
    screw_point = rotate(90, FORWARD_VEC)(screw_point)
    screw_point = rotate(270 - dash_link_tilt - tilt_angle, RIGHT_VEC)(screw_point)
    screw_point += cube([dash_link_gap - 1, 23, 19.3])
    screw_point = translate([-(dash_link_gap - 1) / 2, 7, 10])(screw_point)
    
    model = mount_point + screw_point

    return model

if __name__ == '__main__':
    model = dash_mount_upper()

    scad_render_to_file(model, '_%s.scad'% __file__[:-3])

