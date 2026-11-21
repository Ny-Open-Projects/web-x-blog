---
title: [Q415] 启动优化:惰性导入、__pycache__ 与 pyc 失效
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q415 · 启动优化:惰性导入、__pycache__ 与 pyc 失效

> 难度:★★★★☆ | 标签:import, 启动优化, pyc

**问**:CLI 工具冷启动 800ms,如何系统性缩短?`.pyc` 缓存什么时候失效?为什么 `python -S`、`-X importtime` 是排查标配?有人删了 `__pycache__` 为什么反而"修好了"问题?

**答**:启动时间三要素:解释器自身初始化(可用 `-S` 跳过 site,`-X frozen_modules` 控制 stdlib 冻结模块)、import 图大小(`-X importtime` 逐项列出每个模块的 self/cumulative 微秒,树状排掉最贵的)、以及模块顶层副作用。`.pyc` 失效判定是**源文件 mtime + size** 与 pyc 头里的元数据比对(PEP 552 支持哈希模式,`--invalidation-mode checked/unchecked-hash`),注意 CI 里 mtime 漂移和只读文件系统(无 cache 目录)是常见坑。"删 pycache 修好问题"通常是 pyc 与源码不一致的陈旧缓存(mtime 粒度或拷贝导致),或是旧字节码版本残留。真正的惰性导入模式:把 import 移进函数(代价是首次调用慢 + 掩盖循环依赖)、`importlib.util.LazyLoader`、或 PEP 690 式 lazy import(目前未进主线,但 `python -X importtime` + 按需 import 是 3.12 现实方案)。

```python
# file: code/01_语言核心与底层/q415_import_startup.py
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
```

**追问**:1) PEP 552 unchecked-hash 模式的取舍?——跳过源码校验获得最快导入,但源码改了也不重编,只适合不可变部署(镜像内)。2) `__pycache__` 在 zipimport/冻结模块下还有效吗?——frozen stdlib 模块直接内嵌字节码,zipimport 支持 pyc 但不能写回,只读环境需预编译。
