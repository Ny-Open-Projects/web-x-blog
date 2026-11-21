import importlib.util
import marshal
import os
import py_compile
import sys
import time

# 1) 编译出 pyc,检查其头部元数据
src = __file__
cache = py_compile.compile(src, cfile="/tmp/_demo_q415.pyc", doraise=True)
with open(cache, "rb") as f:
    header = f.read(16)
magic, flags, mtime, size = header[:4], int.from_bytes(header[4:8], "little"), \
    int.from_bytes(header[8:12], "little"), int.from_bytes(header[12:16], "little")
st = os.stat(src)
print("pyc mtime matches source:", int(st.st_mtime) == mtime, "| size:", st.st_size == size)
print("flags:", flags, "0=mtime 校验 1=hash 校验")

# 2) 用 importtime 思路测量一次真实 import 成本
t0 = time.perf_counter()
importlib.import_module("json")
print("import json took", round((time.perf_counter() - t0) * 1e6), "us")

# 3) 惰性导入:import 延迟到首次属性访问
from importlib.util import LazyLoader

def lazy_module(name):
    spec = importlib.util.find_spec(name)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    LazyLoader.exec_module  # noqa: 说明 LazyLoader 需包 loader
    loader_real = LazyLoader(spec.loader)
    spec.loader = loader_real
    loader_real.exec_module(module)
    return module

t0 = time.perf_counter()
m = lazy_module("xml.etree.ElementTree")
print("lazy import fast:", round((time.perf_counter() - t0) * 1e6), "us")
t0 = time.perf_counter()
m.parse   # 首次属性访问触发真实执行
print("first touch:", round((time.perf_counter() - t0) * 1e6), "us")
