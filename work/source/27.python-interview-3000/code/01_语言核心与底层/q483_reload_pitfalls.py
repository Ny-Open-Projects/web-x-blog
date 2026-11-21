import importlib
import os
import sys
import tempfile

def write_module(path, value_expr):
    with open(path, "w", encoding="utf-8") as f:
        f.write(f"VALUE = {value_expr}\nITEMS = []\n")

if __name__ == "__main__":
    d = tempfile.mkdtemp()
    path = os.path.join(d, "hotmod.py")
    write_module(path, "1")
    sys.path.insert(0, d)
    import hotmod
    hotmod.ITEMS.append("kept by reference")

    write_module(path, "2")               # 模拟修改源码
    importlib.reload(hotmod)              # 重新执行模块顶层
    print("VALUE reloaded:", hotmod.VALUE)
    print("ITEMS after reload:", hotmod.ITEMS)   # 顶层重跑:旧列表连同数据失联
    print("reload returns same module:", importlib.reload(hotmod) is hotmod)
    sys.path.pop(0)
