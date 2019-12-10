from solid import *
from solid.utils import *

from constants import *
from chamfer import *

x: float = 97
y: float = 25
z: float = 17
t: float = 5

def base():
    model = cube([x, y, t])

    tab = cube([t, y, z + t])
    tab += translate([t, y, t])(rotate(90, DOWN_VEC)(chamfer(y, 3)))

    model += tab
    model += translate([x, y])(rotate(180, UP_VEC)(tab))

    model -= translate([0, y / 2, z])(
        rotate(90, FORWARD_VEC)(cylinder(d = screw_d, h = x))
    )

    model = forward(y)(rotate(180, RIGHT_VEC)(model))

    return model

def bucket_headlight_rear_join():
    model = base()
    
    cx: float = 3
    tz: float = 20

    upper_tab = cube([t, y, tz])
    upper_tab += translate([t, y])(rotate(90, DOWN_VEC)(chamfer(y, cx)))
    upper_tab += rotate(90, UP_VEC)(chamfer(y, cx)) 

    offset = 15

    model += right(cx + offset)(upper_tab)
    model += right(x - t - cx - offset)(upper_tab)

    return model

if __name__ == '__main__':
    model = bucket_headlight_rear_join();

    scad_render_to_file(model, '_%s.scad'% __file__[:-3])

