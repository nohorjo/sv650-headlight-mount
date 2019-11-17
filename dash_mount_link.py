from solid import *
from solid.utils import *

from constants import *
from references import MoveablePoint

def dash_mount_link():
    base_x: float = 30
    height: float = 130
    end_height: float = 15
    shaft_x: float = 20
    y_chamfer: float = 5

    p = MoveablePoint()
    model = polygon([
        p.val(),
        p.right(base_x).val(),
        p.up(end_height).val(),
        p.left((base_x - shaft_x) / 2).up(y_chamfer).val(),
        p.up(height - (2 * (end_height + y_chamfer))).val(),
        p.right((base_x - shaft_x) / 2).up(y_chamfer).val(),
        p.up(end_height).val(),
        p.left(base_x).val(),
        p.down(end_height).val(),
        p.right((base_x - shaft_x) / 2).down(y_chamfer).val(),
        p.down(height - (2 * (end_height + y_chamfer))).val(),
        p.left((base_x - shaft_x) / 2).down(y_chamfer).val(),
    ])
    
    screw_hole_count = 3
    holes = circle(d = screw_d)
    for i in range(screw_hole_count):
        holes += right(i * (base_x / screw_hole_count))(circle(d = screw_d))

    holes = right((base_x / screw_hole_count) / 2)(holes)

    t: float = 6
    model -= forward(end_height / 2)(holes)
    model -= forward(height - (end_height / 2))(holes)
    model = linear_extrude(t)(model)

    gap: float = dash_link_thick - (2 * t)
    model = model + up(gap + t)(model)

    y_chamfer: float = 3
    support_thick: float = 10

    p = MoveablePoint()
    support = polygon([
        p.val(),
        p.right(support_thick + (2 * y_chamfer)).val(),
        p.up(y_chamfer).left(y_chamfer).val(),
        p.up(gap - (2 * y_chamfer)).val(),
        p.right(y_chamfer).up(y_chamfer).val(),
        p.left(support_thick + (2 * y_chamfer)).val(),
        p.down(y_chamfer).right(y_chamfer).val(),
        p.down(gap - (2 * y_chamfer)).val(),
    ])

    support = linear_extrude(height - (2 * end_height))(support)
    support = rotate(90, LEFT_VEC)(support)
    support = translate([(base_x - support_thick - (2 * y_chamfer)) / 2, end_height, gap + t])(support)

    model += support

    return model

if __name__ == '__main__':
    model = dash_mount_link()

    scad_render_to_file(model, '_%s.scad'% __file__[:-3])

