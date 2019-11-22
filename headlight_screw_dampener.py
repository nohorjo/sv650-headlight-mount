from solid import *
from solid.utils import *

from constants import *

if __name__ == '__main__':
    h: float = 9

    model = cylinder(h=h, d=6) - cylinder(h=h, d=screw_d + 0.5)

    scad_render_to_file(model, '_%s.scad' % __file__[:-3])

