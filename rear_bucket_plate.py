from solid import *
from solid.utils import *

from constants import *

total_y: float = 114

def shell(t: float = 0):
    big_r: float = 44 + t
    small_r: float = 20 + t

    y: float = total_y - big_r + (t * 2)

    model = circle(r = small_r)
    model = left(big_r - small_r)(model) + right(big_r - small_r)(model)
    model = forward(small_r)(model)
    model += forward(y)(circle(r = big_r))

    model = hull()(model)


    return model

def rear_bucket_plate():
    h: float = 3.5
    t: float = 3
    model = linear_extrude(h)(shell(t))
    lip: float = 1.5
    model += up(h)(
        linear_extrude(lip)(shell(t))
        - forward(t)(linear_extrude(lip)(shell()))
    )

    tab_hole = cube([7, rear_join_y + 2, h])

    sep: float = 28
    model -= translate([-2.75, 52])(
        left(sep)(tab_hole)
        + right(sep)(tab_hole)
    )

    cable_hole_d: float = 35
    model -= forward(total_y - (cable_hole_d / 2))(cylinder(h = h, d = cable_hole_d))


    return model

if __name__ == '__main__':
    model = rear_bucket_plate()

    scad_render_to_file(model, '_%s.scad'% __file__[:-3])

