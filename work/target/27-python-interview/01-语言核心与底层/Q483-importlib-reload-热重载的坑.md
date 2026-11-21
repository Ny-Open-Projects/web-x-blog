---
title: [Q483] importlib.reload 热重载的坑
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q483 · importlib.reload 热重载的坑

> 难度:★★★★ | 标签:import, reload

**问**:改了模块源码后 importlib.reload 能热更新吗?为什么重载后旧对象还在被引用?

**答**:reload 会重新执行模块顶层代码、用新值覆盖模块字典,但有两个必然的坑:1) reload 前从模块拿出去的引用(类、函数、可变状态)仍指向旧对象,「import 一次到处用」的代码不会自动切换;2) 顶层重新执行意味着可变全局状态被重置,模块里 `ITEMS = []` 会让旧列表连同其中的数据一起失联。可靠的工程做法是:热更新只用于开发调试(配合 IPython autoreload 或 uvicorn --reload 这类进程级重启),生产配置用「读文件→重建对象→原子替换」而不是 reload;跨模块引用类和函数时,统一从模块属性访问而不是 from-import 缓存。

```python
# file: code/01_语言核心与底层/q483_reload_pitfalls.py
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
```

**追问**:1) reload 会重新执行被 import 的子模块吗?——不会,sys.modules 里已有的子模块直接复用;要级联重载需要自己按依赖序逐个 reload,这正是热重载工具复杂的根源。2) reload 后旧引用为什么还是旧对象?——reload 在原模块对象上重跑代码体,sys.modules 条目不变;其他模块 from-import 拿走的名字仍指向旧对象,只有通过模块属性访问才能看到新值。3) 命名空间怎么处理?——在原 __dict__ 上重执行模块体,新代码不再定义的旧名字会残留(不清空),幽灵属性是 reload 特有的坑。4) 生产陷阱?——reload 后类对象身份变化,isinstance/pickle 失效;开发图省事用 reload 调试,把不可复现状态带上生产——工程上应使用进程级重启。
