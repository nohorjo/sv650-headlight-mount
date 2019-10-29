from solid import *
from solid.utils import *

from constants import *
from super_hole import *

def fork():
    model = cylinder(h = 200, d = fork_d)
    model = right(fork_dist)(model)
    model += cylinder(h = 200, d = fork_d)
    model = background(model)
    
    return model

def indicator_hole(_debug = False):
    model = cube([10, 26, 5])

    if _debug:
        return debug(model)
    else:
        return super_hole(model, 'indicator_hole')

if __name__ == '__main__':
    model = fork()
    scad_render_to_file(model, '_%s.scad'% __file__[:-3])

