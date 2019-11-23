import math

from solid import *
from solid.utils import *

from constants import *
from references import bucket
from dash_mount_upper import dash_mount_upper, trapezium, lower_plug_d
from dash_mount_link import dash_mount_link
from bucket_headlight_join import  bucket_headlight_join

if __name__ == '__main__':
    tilt_angle: float = 60

    model = translate([0, -68, 175])(
        rotate(tilt_angle, RIGHT_VEC)(
            rotate(180, FORWARD_VEC)(dash_mount_upper())
        )
    )

    link = dash_mount_link()
    link = rotate(90, FORWARD_VEC)(link)
    link = rotate(120, RIGHT_VEC)(link)
    link = translate([-dash_link_thick / 2, 10, 61])(link)

    model += link

    model += translate([0, 31, -28])(
        rotate(90, RIGHT_VEC)(
            rotate(90, UP_VEC)(bucket_headlight_join())
        )
    )

    scad_render_to_file(model, '_%s.scad'% __file__[:-3])

