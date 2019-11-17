from solid import *
from solid.utils import *

from constants import *
from references import bucket

def dash_mount_lower():
    x: float = 175
    base = cylinder(h = x, d = 35) - hole()(cylinder(h = x, d = 10))
    base = rotate(90, FORWARD_VEC)(base)
    base = translate([-x / 2, 40 + (35 / 2)])(base)


    base += translate([0, 50, -15])(
        rotate(60, LEFT_VEC)(
            cylinder(h = 35, d = x)
            - left(100)(cube(200))
        )
    )
    base = hull()(base)

    model = base

    factor = 1.05
    model += forward(100)(rotate(90, RIGHT_VEC)(bucket()))
    model -= forward(100)(scale([factor, factor, factor])(rotate(90, RIGHT_VEC)(bucket(False))))

    return model

if __name__ == '__main__':
    model = dash_mount_lower()

    scad_render_to_file(model, '_%s.scad'% __file__[:-3])

