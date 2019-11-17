import math

from solid import *
from solid.utils import *

from constants import *
from references import bucket
from dash_mount_lower import dash_mount_lower
from dash_mount_upper import dash_mount_upper, trapezium, lower_plug_d

if __name__ == '__main__':
    tilt_angle: float = 60
    rise: float = 100

    model = up(rise)(rotate(tilt_angle, RIGHT_VEC)(dash_mount_upper())) + dash_mount_lower()

    factor = 1.05
    model += forward(100)(rotate(90, RIGHT_VEC)(bucket()))
    model -= forward(100)(scale([factor, factor, factor])(
        rotate(90, RIGHT_VEC)(bucket(False)))
    )

    scad_render_to_file(model, '_%s.scad'% __file__[:-3])

