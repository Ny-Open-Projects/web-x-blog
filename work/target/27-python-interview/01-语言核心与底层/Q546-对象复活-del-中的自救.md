---
title: [Q546] 对象复活:__del__ 中的自救
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q546 · 对象复活:__del__ 中的自救

> 难度:★★★★★ | 标签:GC, __del__

**问**:__del__ 里把 self 存到全局变量会发生什么?为什么这是所有实现里最危险的操作?

**答**:__del__ 执行时对象刚「不可达」,但方法体里重新建立引用(存全局、挂到活对象上)会让它「复活」:CPython 引用计数路径下对象实际不释放,再次失去引用时是否二次调用 __del__ 属于实现细节(PEP 442 后循环 GC 路径有 finalized 标志但行为仍微妙)。危险点:对象状态在「终结前后」不一致、依赖 __del__ 恰好一次的清理逻辑(关连接、删文件)被破坏、其他实现(PyPy)行为不同。规范:__del__ 禁止复活、禁止访问可能已拆卸的全局,真正的清理用 weakref.finalize 或显式 close。

```python
# file: code/01_语言核心与底层/q546_resurrection.py
import gc

class Phoenix:
    def __del__(self):
        print("__del__ running")
        globals()["keep"] = self          # 复活:重新建立引用

if __name__ == "__main__":
    p = Phoenix()
    del p                                 # 计数归零,触发 __del__
    print("resurrected as:", type(keep).__name__)
    keep = None                           # 再次失去引用
    gc.collect()
    print("behavior after resurrection is implementation-defined — do not rely on it")
```

**追问**:1) CPython 怎么防止无限复活循环?——GC 路径给对象打 finalized 标志,终结器对同一对象最多执行一次(除非期间又复活重置状态),但引用计数路径的时序仍依赖实现,写代码必须当它不可靠。2) 什么是对象复活?——__del__/weakref 回调里把 self 存进全局,对象在终结后重新可达;3.4+ PEP 442 让循环引用也能安全终结,复活者被提升到老年代按普通对象继续活。3) PEP 442 后的流程?——先收集待终结循环、统一调用终结器、复活者保留、其余销毁;gc.garbage 常态为空,只在不可终结场景才有内容。4) 生产陷阱?——复活对象带着已释放资源被继续调用;依赖 __del__ 释放连接不可靠,必须 with/close 显式管理;终结器只做日志与告警,不做自救。
