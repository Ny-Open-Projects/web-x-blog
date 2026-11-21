---
title: [Q481] import 的完整流程:finder 与 loader
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q481 · import 的完整流程:finder 与 loader

> 难度:★★★★ | 标签:import, 模块

**问**:import 一条语句背后经过哪几步?ModuleSpec、finder、loader 各自的职责是什么?

**答**:五步:1) 查 sys.modules 缓存,命中直接返回;2) 依次询问 sys.meta_path 里的 finder,每个 finder 尝试产出 ModuleSpec(模块的元数据:名字、origin 路径、loader);3) 拿到 spec 后创建模块对象并登记进 sys.modules(先登记再执行,这是循环导入时能拿到「半成品模块」的原因);4) loader.exec_module 执行模块顶层代码,填充模块命名空间;5) 把模块对象绑定到当前命名空间的名字上。理解这条流水线才能解释循环导入、懒加载、meta_path 拦截等所有导入问题。

```python
# file: code/01_语言核心与底层/q481_import_flow.py
import importlib.util
import sys

def explain(name):
    spec = importlib.util.find_spec(name)
    print(f"module {name}:")
    print("  origin :", spec.origin)
    print("  loader :", type(spec.loader).__name__)
    print("  cached :", spec.cached)

if __name__ == "__main__":
    print("meta_path finders:")
    for f in sys.meta_path:
        print("  -", f.__name__ if isinstance(f, type) else type(f).__name__)
    explain("json")
    m = __import__("json")
    print("registered in sys.modules:", sys.modules["json"] is m)
```

**追问**:1) 为什么模块对象在执行前就进 sys.modules?——保证循环导入时另一方 import 拿到的是同一个(半初始化的)模块对象而不是再次触发导入,递归导入因此不死循环但可能 AttributeError。2) 循环导入为什么有时只报 AttributeError?——半初始化模块里尚未定义的属性访问得到 AttributeError;若在模块顶层反过来调用对方还没执行的函数,才升级为 ImportError(cannot import from partially initialized module)。3) finder/loader 的职责怎么分?——find_spec 产出 spec(名字、loader、origin),loader.create_module 建命名空间、exec_module 执行代码体,导入机制随后写 sys.modules 并把模块挂到父包属性上。4) 生产陷阱?——__init__.py 塞重初始化加剧循环导入;热重载工具「删 sys.modules 再 import」造成同名类两个对象共存,isinstance 与 pickle 全部失效。
