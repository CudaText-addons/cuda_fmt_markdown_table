import os
import re
import json
from .simple_markdown import table
from cuda_fmt import get_config_filename

def options():
    fn = get_config_filename('Markdown Table Format')
    if os.path.isfile(fn):
        s = open(fn, 'r').read()
        #del // comments
        s = re.sub(r'(^|[^:])//.*'  , r'\1', s)           
        d = json.loads(s)
        
        op_margin = d.get("margin", 1)
        op_padding = d.get("padding", 0)
        
        s = d.get("default_justify", "L")
        op_just = table.Justify.LEFT if s=="L" else table.Justify.RIGHT if s=="R" else table.Justify.CENTER
        
        return op_margin, op_padding, op_just 
    else:
        return 1, 0, table.Justify.LEFT
    

def do_format(text):
    op_margin, op_padding, op_just = options()
    return table.format(text,
                        margin = op_margin, 
                        padding = op_padding,
                        default_justify = op_just,
                        )
