---
title: [Q416] 命名空间包:没有 __init__.py 的包是怎么回事?
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q416 · 命名空间包:没有 __init__.py 的包是怎么回事?

> 难度:★★★★☆ | 标签:PEP 420, import, 打包

**问**:一个目录没有 `__init__.py`,`import` 居然成功了,`__file__` 是 None,`__path__` 是 list——这背后是什么机制?它和 regular package、以及"两个发行版合并一个包"的场景有什么关系?

**答**:PEP 420 引入 namespace package:当 finder 沿 `sys.path` 找目录且目录无 `__init__.py` 时,不再报错而是记录为一个"portion",最终合成一个 `NamespacePath` 动态对象作为 `__path__`,该模块 `__file__` 为 `None`、`__loader__` 是 `_NamespaceLoader`。它解决的正是"一个顶层包名被多个独立分发(split distribution)共享"——比如 `google.protobuf` 与 `google.auth` 各自只装 `google/` 的一部分。代价是错误容忍度过高:**忘写 `__init__.py` 的普通包会被静默当成命名空间包**,导致部分工具(setuptools 自动发现、mypy、运行期 `__file__` 依赖)行为异常;打包侧需要 `packages = find_namespace_packages:` 而非普通 find。排查时看 `pkg.__path__` 的 repr:`_NamespacePath` 即命名空间包。

```python
# file: code/01_语言核心与底层/q416_namespace_pkg.py
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
```

**追问**:1) `__init__.py` 存在时还能合并 portion 吗?——不能,regular package 的 `__path__` 在初始化时固化为单一路径,PEP 420 只对无 `__init__.py` 目录生效。2) 为什么 typing/mypy 对命名空间包支持麻烦?——静态工具需要在 import 前解析 portion 布局,动态合成的 `__path__` 无法提前静态确定。
