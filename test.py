from functools import reduce
from solid import *
from solid.utils import *

from constants import *
from super_hole import *

h: float = 70
t: float = 5
screw_m_y: float = 15

def screw_mount():
    model = cube([t, screw_m_y, h])

    c: float = 5
    d: float = 12.5
    hole = cylinder(h = t, d = 3)
    holes = hole
    for i in range(c - 1):
        holes += forward((i + 1) * d)(hole)
    holes = rotate(90, FORWARD_VEC)(holes)
    holes = rotate(90, RIGHT_VEC)(holes)
    holes = forward(screw_m_y / 2)(holes)
    holes = up((h - ((c - 1) * d)) / 2)(holes)

    model -= holes

    return model

def fork_mount():
    outer_d = fork_d + (2 * t)
    
    model = cylinder(h = h, d = outer_d)
    model -= cylinder(h = h, d = fork_d)
    model -= back(outer_d / 2)(cube(h))
    model = rotate(180)(model)

    mounts = forward(outer_d / 2 - 2)(screw_mount())
    mounts += back(outer_d / 2 + screw_m_y - 2)(screw_mount())

    r = 5
    arcs = translate([
        r + t,
        r + (outer_d / 2) - 2.5,
    ])(arc_inverted(rad = r, start_degrees = 180, end_degrees = 255))
    arcs += translate([
        r + t,
        -(r + (outer_d / 2) - 2.5),
    ])(arc_inverted(rad = r, start_degrees = 180, end_degrees = 90))

    mounts += linear_extrude(h)(arcs)

    model += mounts

    return model

def main_mount():
    model = fork_mount()

    return model

if __name__ == '__main__':
    model = main_mount()
    model += left(1)(mirror(LEFT_VEC)(fork_mount()))

    scad_render_to_file(model, '_%s.scad'% __file__[:-3])

