from solid import *
from solid.utils import *

from constants import *

if __name__ == '__main__':
    t: float = 5

    model = cube([bucket_tab_x, 30, t])
    model -= translate([bucket_tab_screw_offset_x, 10, -10])(
        cylinder(d = screw_d, h = t + 10)

        + right(bucket_tab_x - (bucket_tab_screw_offset_x * 2))(cylinder(d = screw_d, h = t + 10))
    )
    scad_render_to_file(model, '_%s.scad'% __file__[:-3])

