from solid import *
from solid.utils import *

from constants import *
from references import MoveablePoint

if __name__ == '__main__':
    base_x: float = 20
    height: float = 130
    end_height: float = 15
    shaft_x: float = 10
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

    model -= forward(end_height / 2)(holes)
    model -= forward(height - (end_height / 2))(holes)
    model = linear_extrude(6)(model)

    scad_render_to_file(model, '_%s.scad'% __file__[:-3])

