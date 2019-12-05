import math
from solid import *
from solid.utils import *

from constants import *
from super_hole import *
from references import *
from chamfer import *

def bucket_headlight_join():
    outer_r: float = 86.5
    thick: float = 3
    base_h: float = thick + 3
    inner_r: float = outer_r - (2 * thick)
    model = circle(r = outer_r + thick)
    model -= circle(r = inner_r)
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


    model = rotate(40, UP_VEC)(model)
    model = rotate(2 * math.degrees(math.asin(22 / inner_r)), UP_VEC)(model)
    model = rotate(180, RIGHT_VEC)(model)

    top_arc_angle: float = 2 * math.degrees(math.asin(44 / inner_r))
    top_arc = lambda rad, bigger = False: arc(
            rad = rad,
            start_degrees = -10 - top_arc_angle - (2 if bigger else 0),
            end_degrees = 10 + top_arc_angle + (2 if bigger else 0)
    )

    top_part_gap: float = 3
    top_part = top_arc(outer_r + thick)
    top_part -= top_arc(outer_r - thick - top_part_gap, True)
    top_part -= top_arc(outer_r) - top_arc(outer_r - top_part_gap)
    top_part = linear_extrude(20)(top_part)

    bucket_screw_holes = cylinder(h = 15, d = 6)
    bucket_screw_holes = rotate(90, FORWARD_VEC)(bucket_screw_holes)
    bucket_screw_holes = translate([outer_r - 10, 0, 13])(bucket_screw_holes)
    bucket_screw_holes = rotate(top_arc_angle, UP_VEC)(bucket_screw_holes) + rotate(top_arc_angle, DOWN_VEC)(bucket_screw_holes)

    top_part -= bucket_screw_holes
    top_part = render()(top_part)

    if top_part_gap >= 4:
        t = top_part_gap - thick
        top_part += down(base_h)(linear_extrude(base_h + thick)(
            top_arc(inner_r + thick) - top_arc(inner_r - t - 1, True)
        ))

    holes = cylinder(h = dash_link_gap, d = screw_d)
    for i in range(dash_screw_hole_count):
        holes += right(i * (dash_link_base_x / dash_screw_hole_count))(
            hole()(cylinder(h = dash_link_gap, d = screw_d))
        )

    def screw_point_movements(model):
        model = rotate(90, RIGHT_VEC)(model)
        model = rotate(90, FORWARD_VEC)(model)
        model = rotate(dash_link_tilt - 90, BACK_VEC)(model)

        return model

    screw_point = cube([30, 17, dash_link_gap - 1])
    screw_point -= translate([10 / 2, 20 / 2])(holes)
    screw_point = screw_point_movements(screw_point)
    screw_point += rotate(10, FORWARD_VEC)(
        screw_point_movements(cube([26, 17, dash_link_gap - 1]))
    )
    screw_point = translate([outer_r, dash_link_gap / 2, 26 - (thick * 2)])(screw_point)

    top_part += screw_point

    model += top_part

    return model

if __name__ == '__main__':
    model = bucket_headlight_join()

    scad_render_to_file(model, '_%s.scad'% __file__[:-3])

