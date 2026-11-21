"""__all__ 与星号导入治理:import * 到底拿走什么。"""
import pathlib
import sys
import tempfile

MODULE_BODY = """import os
import sys

API_VALUE = "public"
_INTERNAL = "hidden"
{all_line}
"""


def make_module(root, name, has_all):
    all_line = '__all__ = ["API_VALUE"]' if has_all else ""
    (pathlib.Path(root) / f"{name}.py").write_text(
        MODULE_BODY.format(all_line=all_line), encoding="utf-8")


def star_import_names(root, modname):
    sys.modules.pop(modname, None)
    sys.path.insert(0, root)
    try:
        ns = {}
        exec(f"from {modname} import *", ns)
        return sorted(k for k in ns if not k.startswith("__"))
    finally:
        sys.path.remove(root)


if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as tmp:
        make_module(tmp, "mod_no_all", has_all=False)
        make_module(tmp, "mod_with_all", has_all=True)
        print("无 __all__ 的 import *:", star_import_names(tmp, "mod_no_all"))
        print("有 __all__ 的 import *:", star_import_names(tmp, "mod_with_all"))
    print("无 __all__ 时连 import 进来的 os、sys 都被带走——这就是星号导入的污染面")
