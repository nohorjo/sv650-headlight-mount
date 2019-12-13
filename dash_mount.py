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
from rear_plate_secure import rear_plate_secure

if __name__ == '__main__':
    model = translate([0, -24, 197])(
        rotate(90 - tilt_angle, RIGHT_VEC)(
            rotate(180, FORWARD_VEC)(color('blue')(dash_mount_upper()))
        )
    )

    link = color('green')(dash_mount_link())
    link = rotate(90, FORWARD_VEC)(link)
    link = rotate(dash_link_tilt, RIGHT_VEC)(link)
    link = translate([-dash_link_thick / 2, 10, 61])(link)

    model += link

    model += translate([0, 31, -28])(
        rotate(90, RIGHT_VEC)(
            rotate(90, UP_VEC)(color('yellow')(bucket_headlight_join()))
        )
    )

    model += translate([-50, -10, -43])(rotate(90, RIGHT_VEC)(
        color('red')(bucket_headlight_rear_join())
        + translate([44 + (2 * 2), 25 + 53, 34 + 3])(rotate(180, RIGHT_VEC)(color('white')(rear_bucket_plate())))
        + translate([23.5, 0, 37.5])(color('black')(rear_plate_secure()))
    ))

    scad_render_to_file(model, '_%s.scad'% __file__[:-3])

