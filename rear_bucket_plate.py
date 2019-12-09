from solid import *
from solid.utils import *

from constants import *

def rear_bucket_plate():
    t: float = 5
    tab_overlap = 50
    x = 70

    model = cube([x, tab_overlap, t])
    model -= translate([(x / 2) - bucket_tab_screw_offset_x, 10, -10])(
        cylinder(d = screw_d, h = t + 10)
        + right(bucket_tab_x - (bucket_tab_screw_offset_x * 2))(cylinder(d = screw_d, h = t + 10))
    )

    return model

if __name__ == '__main__':
    model = rear_bucket_plate()

    scad_render_to_file(model, '_%s.scad'% __file__[:-3])

