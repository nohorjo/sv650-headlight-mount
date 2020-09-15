from solid import *
from solid.utils import *

from references import MoveablePoint
from super_hole import *

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

def headlamp_part():
    p = MoveablePoint()
    hole = polygon([
        p.val(),
        p.right(40).val(),
        p.up(15).val(),
        p.left(5).val(),
        p.up(29).val(),
        p.left(14).val(),
        [0, 7],
    ])
    hole = linear_extrude(5)(hole)
    hole += translate([7.5, 9.5, -16])(linear_extrude(25)(
        back(1.5)(circle(d = 6))
        + translate([9, 1.5])(circle(d = 6))
        + right(18)(circle(d = 6))
    ))
    hole += translate([0, 4, -10.5])(cube([90, 12.5, 4.5]))

    hole = super_hole(hole, 'headlamp_part_hole')

    model = translate([0, -3, -3])(linear_extrude(11)(polygon([
        p.reset().val(),
        p.right(42).val(),
        p.up(18).val(),
        p.left(7).val(),
        p.up(29).val(),
        p.left(14).val(),
        [0, 10],
    ]))) - hole

    model = rotate(90, BACK_VEC)(model)
    model += translate([3, 0, 0])(cube([40, 30, 70]))

    return model

def dash_mount_upper():# {{{
    t: float = 3
    upper_plug_d: float = 8
    plug_h: float = 10

    plug_holes = lambda t: (
        right(trapezium["side"])(cylinder(h = plug_h, d = upper_plug_d  + (t * 2)))
        + cylinder(h = plug_h, d = lower_plug_d + (t * 2)) 
    )

    plugs_mount = hull()(plug_holes(t)) - super_hole(plug_holes(0), 'plug_holes')

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
    mount_point -= forward(25)(super_hole(cylinder(h = 20, d = 10), 'another_hole'))
    mount_point -= translate([-100, -100, -200])(super_hole(cube([200, 200, 200]), 'dash_cube'))

    return mount_point# }}}

if __name__ == '__main__':
    model = dash_mount_upper()
    model = rotate(180, FORWARD_VEC)(model)
    model = rotate(60, RIGHT_VEC)(model)
    model = translate([20, 0, 45])(model)

    model += headlamp_part()

    p = MoveablePoint()
    b_hole = linear_extrude(50)(polygon([
        p.forward(-20).val(),
        p.forward(43).val(),
        p.rotate(60).forward(57).val(),
        p.rotate(-90).forward(50).val(),
        p.down(60).val(),
        p.set(x = 0).val(),
    ]))
    b_hole = rotate(90, RIGHT_VEC)(b_hole)
    b_hole = rotate(90, UP_VEC)(b_hole)
    b_hole = rotate(30, RIGHT_VEC)(b_hole)
    b_hole = translate([3, 7, -5])(b_hole)
    b_hole = super_hole(b_hole, 'b_hole')

    model -= b_hole

    scad_render_to_file(model, '_%s.scad'% __file__[:-3])

