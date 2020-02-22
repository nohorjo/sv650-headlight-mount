from solid import *
from solid.utils import *

from constants import *
from chamfer import *

x: float = 97
z: float = 17
t: float = 5

def base():
    model = cube([x, rear_join_y, t])

    tab = cube([t, rear_join_y, z + t])
    tab += translate([t, rear_join_y, t])(rotate(90, DOWN_VEC)(chamfer(rear_join_y, 3)))

    model += tab
    model += translate([x, rear_join_y])(rotate(180, UP_VEC)(tab))

    model -= translate([0, rear_join_y / 2, z])(
        rotate(90, FORWARD_VEC)(cylinder(d = screw_d, h = x))
    )

    model = forward(rear_join_y)(rotate(180, RIGHT_VEC)(model))

    return model

def bucket_headlight_rear_join():
    model = base()
    
    cx: float = 3
    tz: float = 53

    upper_tab = cube([t, rear_join_y, tz])
    upper_tab += translate([t, rear_join_y])(rotate(90, DOWN_VEC)(chamfer(rear_join_y, cx)))
    upper_tab += rotate(90, UP_VEC)(chamfer(rear_join_y, cx)) 

    upper_tab -= translate([0, rear_join_y / 2, tz - 11.5])(rotate(90, FORWARD_VEC)(cylinder(h = t, d = screw_d)))

    offset = 15

    model += right(cx + offset)(upper_tab)
    model += right(x - t - cx - offset)(upper_tab)

    return model

if __name__ == '__main__':
    model = bucket_headlight_rear_join();

    scad_render_to_file(model, '_%s.scad'% __file__[:-3])

