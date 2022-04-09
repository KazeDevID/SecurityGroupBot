from glob import glob
from importlib import import_module

mod_paths = glob("PunyaChael/modules/*.py")
MODULES = [
    "PunyaChael.modules." + f.split("/")[-1][:-3]
    for f in mod_paths
    if not f.endswith("__.py")  # to exclude __init__.py
]
import_module("PunyaChael.modules.__main__")
