---
title: [Q458] 模块级 __getattr__:PEP 562 懒加载
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q458 · 模块级 __getattr__:PEP 562 懒加载

> 难度:★★★☆ | 标签:模块, 懒加载

**问**:模块也能定义 __getattr__?它和函数里的 __getattr__ 时机一样吗,适合什么场景?

**答**:PEP 562 允许模块定义 `__getattr__(name)` 和 `__dir__()`:前者只在「常规属性查找失败」后调用,与类机制同源;后者补全 dir() 输出。典型用途:大包的懒加载子模块(numpy 式的 `np.linalg` 按需导入)、弃用属性的兼容层(访问旧名字时告警并转发)、动态属性只读接口。注意触发条件是属性访问(module.attr),模块内裸名字的查找走 LOAD_NAME,不会经过它;且一旦把值写回模块字典,后续访问就不再进钩子。

```python
# file: code/01_语言核心与底层/q458_module_getattr.py
"""PEP 562:模块级 __getattr__ 与懒加载"""
import sys

def __getattr__(name):
    """常规模块属性查找失败时才会被调用"""
    if name == "HEAVY":
        print("computing HEAVY lazily")
        value = sum(range(10 ** 6))
        globals()["HEAVY"] = value        # 写回模块字典:下次常规查找直接命中
        return value
    raise AttributeError(f"module has no attribute {name!r}")

def __dir__():
    return sorted(set(globals()) | {"HEAVY"})

if __name__ == "__main__":
    me = sys.modules[__name__]
    print("HEAVY in dir:", "HEAVY" in dir(me))
    print(me.HEAVY)                       # 属性访问触发模块级 __getattr__
    print(me.HEAVY)                       # 已写回:不再进钩子
    try:
        me.nope
    except AttributeError as e:
        print(e)
```

**追问**:1) 模块 __getattr__ 与类 __getattr__ 的调用时机一致吗?——一致:都在实例/模块字典、类、基类的常规查找全部失败后调用,所以「缓存写回」能天然短路钩子。2) 为什么写回 globals() 之后钩子不再触发?——钩子只在常规查找失败后调用;写回后属性位于模块 __dict__,LOAD_ATTR 直接命中,这是「惰性计算 + 缓存」的标准模式。3) 模块属性查找的完整路径?——先查模块 __dict__,失败找 md_dict['__getattr__'](模块加载器在加载时绑定),再失败抛 AttributeError;dir() 定制靠模块级 __dir__。4) 生产陷阱?——IDE 与类型检查器看不到动态属性,要配 __dir__ 和 .pyi 存根;钩子里抛普通 Exception 而非 AttributeError,hasattr/getattr 默认值协议被破坏。
