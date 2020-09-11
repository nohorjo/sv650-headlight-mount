from solid import *
from solid.utils import *

from constants import *
from super_hole import *
from references import *

mh: float = 2.5

def mount_part():
    model = circle(d = 26)
    model += forward(13)(square([30, 1], True))
    model = hull()(model)
    model = linear_extrude(mh)(model)
    model += down(25)(cylinder(h = 50, d = 9))

    model = rotate(180, UP_VEC)(model)
    model = forward(10)(model)

    return super_hole(model, 'mount_part')

if __name__ == '__main__':
    p = MoveablePoint()
    y: float = 35
    x: float = 7
    model = linear_extrude(y)(polygon([
        p.val(),
        p.up(30).val(),
        p.up(10).right(x).val(),
        p.up(20).val(),
        p.right(x).val(),
        p.down(24).val(),
        p.down(10).left(x).val(),
        p.set(y = 0).val(),
    ]))
    model = right(y / 2)(rotate(90, BACK_VEC)(model))

    model -= super_hole(forward(50)(cylinder(h = 50, d = 9)), 'bolt')
    model -= up((x - mh) / 2)(mount_part())

    model *= hull()(linear_extrude(40)(
        square([y, 1], True)
        + forward(50)(circle(d = 20))
    ))

    model = minkowski()(model, sphere(r = 3))

    scad_render_to_file(model, '_%s.scad'% __file__[:-3])

