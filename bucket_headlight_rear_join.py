from solid import *
from solid.utils import *

from constants import *
from chamfer import *

if __name__ == '__main__':
    x: float = 100
    y: float = 45
    z: float = 25
    t: float = 5
    tab_y: float = y - 20
    screw_d = 3

    model = cube([x, y, t])
    model += cube([t, tab_y, z + t])
    model += right(x - t)(cube([t, tab_y, z + t]))

    model -= translate([0, tab_y / 2, z])(
        rotate(90, FORWARD_VEC)(cylinder(d = screw_d, h = x))
    )

    model = forward(y)(rotate(180, RIGHT_VEC)(model))

    bucket_tab_x: float = 35
    bucket_tab_z: float = 43
    bucket_tab_screw_offset_x: float = 10
    model += right((x - bucket_tab_x) / 2)(
        cube([bucket_tab_x, t, bucket_tab_z])
        + forward(t)(chamfer(bucket_tab_x, 10))
        + translate([0, -20, bucket_tab_z - t])(
            cube([bucket_tab_x, 20, t])
            + forward(20)(rotate(180, RIGHT_VEC)(chamfer(bucket_tab_x, 10)))
            - translate([bucket_tab_screw_offset_x, 10, -10])(
                cylinder(d = screw_d, h = t + 10)
                + right(bucket_tab_x - (bucket_tab_screw_offset_x * 2))(cylinder(d = screw_d, h = t + 10))
            )
        )
    )

    scad_render_to_file(model, '_%s.scad'% __file__[:-3])

