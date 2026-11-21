"""importlib.resources:包内数据文件的规范访问。"""
import importlib.resources
import os
import sys
import tempfile


def build_pkg(root):
    pkg = os.path.join(root, "resx")
    os.makedirs(pkg)
    with open(os.path.join(pkg, "__init__.py"), "w") as f:
        f.write("")
    with open(os.path.join(pkg, "greeting.txt"), "w", encoding="utf-8") as f:
        f.write("你好,资源文件")
    return "resx"


def read_via_api(pkg_name, pkg_root):
    sys.path.insert(0, pkg_root)
    try:
        mod = importlib.import_module(pkg_name)
        if hasattr(importlib.resources, "files"):         # 3.9+ Traversable
            res = importlib.resources.files(mod).joinpath("greeting.txt")
            return res.read_text(encoding="utf-8")
        return importlib.resources.read_text(mod, "greeting.txt")
    finally:
        sys.path.pop(0)


if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as root:
        pkg_name = build_pkg(root)
        print("读到:", read_via_api(pkg_name, root))
