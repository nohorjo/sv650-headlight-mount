import inspect

from solid import *
from solid.utils import *

def super_hole(model, name):
    fnpart = inspect.stack()[1].filename[:-3].split('/')[-1]
    fn = '.%s_%s.scad'% (fnpart, name)
    content = """
    module %s() {
    %s
    }
    """% (name, scad_render(model))
    with open(fn, 'w') as f:
        f.write(content)
    return hole()(getattr(import_scad(fn), name)())
