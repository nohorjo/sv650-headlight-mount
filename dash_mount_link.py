from solid import *
from solid.utils import *

from constants import *
from references import MoveablePoint

def dash_mount_link():
    height: float = 65
    end_height: float = 15
    shaft_x: float = 20
    y_chamfer: float = 5

    p = MoveablePoint()
    model = polygon([
        p.val(),
        p.right(dash_link_base_x).val(),
        p.up(end_height).val(),
        p.left((dash_link_base_x - shaft_x) / 2).up(y_chamfer).val(),
        p.up(height - (2 * (end_height + y_chamfer))).val(),
        p.right((dash_link_base_x - shaft_x) / 2).up(y_chamfer).val(),
        p.up(end_height).val(),
        p.left(dash_link_base_x).val(),
        p.down(end_height).val(),
        p.right((dash_link_base_x - shaft_x) / 2).down(y_chamfer).val(),
        p.down(height - (2 * (end_height + y_chamfer))).val(),
        p.left((dash_link_base_x - shaft_x) / 2).down(y_chamfer).val(),
    ])
    
    holes = circle(d = screw_d)
    for i in range(dash_screw_hole_count):
        holes += right(i * (dash_link_base_x / dash_screw_hole_count))(circle(d = screw_d))

    holes = right((dash_link_base_x / dash_screw_hole_count) / 2)(holes)

    model -= forward(end_height / 2)(holes)
    model -= forward(height - (end_height / 2))(holes)
    model = linear_extrude(dash_link_end_thick)(model)

    model = model + up(dash_link_gap + dash_link_end_thick)(model)

    y_chamfer: float = 3
    support_thick: float = 10

    p = MoveablePoint()
    support = polygon([
        p.val(),
        p.right(support_thick + (2 * y_chamfer)).val(),
        p.up(y_chamfer).left(y_chamfer).val(),
        p.up(dash_link_gap - (2 * y_chamfer)).val(),
        p.right(y_chamfer).up(y_chamfer).val(),
        p.left(support_thick + (2 * y_chamfer)).val(),
        p.down(y_chamfer).right(y_chamfer).val(),
        p.down(dash_link_gap - (2 * y_chamfer)).val(),
    ])

    support = linear_extrude(height - (2 * end_height))(support)
    support = rotate(90, LEFT_VEC)(support)
    support = translate([(dash_link_base_x - support_thick - (2 * y_chamfer)) / 2, end_height, dash_link_gap + dash_link_end_thick])(support)

    model += support

    gopro_mount = import_stl('lib/Gopro_support_camera_a_vis.stl')
    gopro_mount += forward(9.5)(cube([18, 3, 40]))
    gopro_mount += back(12.5)(cube([18, 3, 40]))

    model += translate([22, 25, 25])(
        rotate(90, RIGHT_VEC)(rotate(90, FORWARD_VEC)(gopro_mount))
    )

    return model

if __name__ == '__main__':
    model = dash_mount_link()

    scad_render_to_file(model, '_%s.scad'% __file__[:-3])

