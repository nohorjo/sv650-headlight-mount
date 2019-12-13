from solid import *
from solid.utils import *

from constants import *

def shell(t: float = 0):
    big_r: float = 44 + t
    small_r: float = 20 + t

    y: float = 114 - big_r + (t * 2) 

    model = circle(r = small_r)
    model = left(big_r - small_r)(model) + right(big_r - small_r)(model)
    model = forward(small_r)(model)
    model += forward(y)(circle(r = big_r))

    model = hull()(model)

    return model

def rear_bucket_plate():
    h: float = 4
    t: float = 3
    model = linear_extrude(h)(shell(t))
    model += up(h)(
        linear_extrude(1)(shell(t))
        - forward(t)(linear_extrude(1)(shell()))
    )

    tab_hole = cube([7, rear_join_y + 2, h])

    sep: float = 28
    model -= translate([-2.75, 52])(
        left(sep)(tab_hole)
        + right(sep)(tab_hole)
    )


    return model

if __name__ == '__main__':
    model = rear_bucket_plate()

    scad_render_to_file(model, '_%s.scad'% __file__[:-3])

