import math

from solid import *
from solid.utils import *

from constants import *
from references import bucket
from dash_mount_upper import dash_mount_upper, trapezium, lower_plug_d
from dash_mount_link import dash_mount_link
from bucket_headlight_join import  bucket_headlight_join
from bucket_headlight_rear_join import bucket_headlight_rear_join
from rear_bucket_plate import rear_bucket_plate

if __name__ == '__main__':
    model = translate([0, -24, 197])(
        rotate(90 - tilt_angle, RIGHT_VEC)(
            rotate(180, FORWARD_VEC)(dash_mount_upper())
        )
    )

    link = dash_mount_link()
    link = rotate(90, FORWARD_VEC)(link)
    link = rotate(dash_link_tilt, RIGHT_VEC)(link)
    link = translate([-dash_link_thick / 2, 10, 61])(link)

    model += link

    model += translate([0, 31, -28])(
        rotate(90, RIGHT_VEC)(
            rotate(90, UP_VEC)(bucket_headlight_join())
        )
    )

    model += translate([-50, -20, -55])(rotate(90, RIGHT_VEC)(
            bucket_headlight_rear_join()
            + translate([16, -20, 46])(rear_bucket_plate())
    ))

    scad_render_to_file(model, '_%s.scad'% __file__[:-3])

