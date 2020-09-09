from solid import *
from solid.utils import *

import math

from constants import *
from super_hole import *

from references import MoveablePoint

if __name__ == '__main__':
    d: float = 6
    x: float = 24.5
    lug = circle(d = d) + right(x - d)(circle(d = d))
    lug = hull()(lug)
    lug = linear_extrude(4)(lug)
    lug += down(25)(super_hole(linear_extrude(50)(
        circle(d = 5.5)
        + right(9)(circle(d = 5.5))
        + right(18)(circle(d = 5.5))
    ), 'dash_mount_bolt_holes'))

    p = MoveablePoint()
    a: float = 60
    s1: float = 35
    s2: float = 12
    s3 = s1 - (s2 / math.tan(math.radians(a)))
    model = linear_extrude(3)(
        minkowski()(
            circle(r = 2),
            polygon([
                p.val(),
                p.left(4).val(),
                p.up(s1).val(),
                p.right(s2 + 3).val(),
                p.down(s3).val(),
            ])
        )
    )

    model += rotate(90 - a, UP_VEC)(
        cube([15, 3, 80])
        + super_hole(
            translate([7.5, -12.5, 75])(rotate(90, LEFT_VEC)(cylinder(d = 5.5, h = 25))),
            'dash_mount_bolt_holes2',
        )
    )

    model += translate([3, 12, -4])(rotate(90, UP_VEC)(lug))

    scad_render_to_file(model, '_%s.scad'% __file__[:-3])

