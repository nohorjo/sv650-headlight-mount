from solid import *
from solid.utils import *

from constants import *

def fork():
    model = cylinder(h = 200, d = 41)
    model = right(fork_dist)(model)
    model += cylinder(h = 200, d = 41)
    model = background(model)
    
    return model

if __name__ == '__main__':
    model = fork()
    scad_render_to_file(model, '_%s.scad'% __file__[:-3])

