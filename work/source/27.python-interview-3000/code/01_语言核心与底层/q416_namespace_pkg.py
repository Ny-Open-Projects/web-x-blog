import os
import sys
import tempfile
import importlib

root = tempfile.mkdtemp()
for sub in ("a_ns", "b_ns"):                       # 两个 portion
    pkg = os.path.join(root, sub, "combo")
    os.makedirs(pkg)
    with open(os.path.join(pkg, "part.py"), "w") as f:
        f.write(f"WHO = '{sub}'\n")                 # 无 __init__.py

sys.path.insert(0, os.path.join(root, "a_ns"))
sys.path.insert(0, os.path.join(root, "b_ns"))

m1 = importlib.import_module("combo.part")
print("module:", m1, "| WHO:", m1.WHO)

pkg_mod = sys.modules["combo"]
print("is namespace package:", pkg_mod.__spec__.submodule_search_locations is not None
      and pkg_mod.__file__ is None)
print("__path__ repr:", type(pkg_mod.__path__).__name__)   # _NamespacePath
print("origin:", pkg_mod.__spec__.origin)                  # None
