import inspect

from solid import *
from solid.utils import *

def super_hole(model, name):
    fn = '.%s_%s.scad'% (inspect.stack()[1].filename[:-3], name)
    content = """
    module %s() {
    %s
    }
    """% (name, scad_render(model))
    with open(fn, 'w') as f:
        f.write(content)
    return hole()(getattr(import_scad(fn), name)())
