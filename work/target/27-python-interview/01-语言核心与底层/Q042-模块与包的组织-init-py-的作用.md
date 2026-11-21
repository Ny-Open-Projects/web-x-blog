---
title: [Q042] 模块与包的组织,__init__.py 的作用
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q042 · 模块与包的组织,__init__.py 的作用

> 难度:★★☆ | 标签:模块, 包

**问**:包和普通目录的区别?__init__.py 里适合放什么?

**答**:含 `__init__.py`(或命名空间包声明)的目录才是传统意义上的包,导入包时会先执行 `__init__.py`,适合:定义 `__all__` 控制星号导入、把子模块 API 上提到包级(`from .sub import func`)、执行包级初始化。`__main__.py` 使包可 `python -m pkg` 运行。`__all__` 只影响 `from pkg import *`,不影响显式导入。

```python
# file: code/01_语言核心与底层/q042_package.py
import os
import sys
import tempfile

root = tempfile.mkdtemp()
pkg = os.path.join(root, "mypkg")
os.makedirs(pkg)
with open(os.path.join(pkg, "__init__.py"), "w") as f:
    f.write("__all__ = ['tool']\nfrom .tool import shout\n")
with open(os.path.join(pkg, "tool.py"), "w") as f:
    f.write("def shout(s):\n    return s.upper() + '!'\n")

sys.path.insert(0, root)

if __name__ == "__main__":
    import mypkg
    print(mypkg.shout("hello"))    # __init__ 里上提的 API
    print(mypkg.__all__)           # 星号导入的白名单
    from mypkg import tool
    print(tool is mypkg.tool)      # 同一模块对象
    print(sorted(os.listdir(pkg)))
```

**追问**:1) 没有 __init__.py 也能导入的目录叫什么?——命名空间包 namespace package,PEP 420 允许分散多目录合成一个包,适合大型单体拆分,但常规库仍建议显式 `__init__.py`。2) __init__.py 里做重活有什么代价?——拖慢所有 import、增加循环导入风险、引入导入期副作用;保持轻量,重初始化暴露成显式函数由入口调用。3) 相对导入什么时候报错?——脚本被直接执行时 `__package__` 为空,`from . import x` 报 attempted relative import with no known parent package;必须以 `python -m pkg` 方式运行。
