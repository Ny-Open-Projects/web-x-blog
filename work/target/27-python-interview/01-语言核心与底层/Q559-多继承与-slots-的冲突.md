---
title: [Q559] 多继承与 __slots__ 的冲突
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q559 · 多继承与 __slots__ 的冲突

> 难度:★★★★★ | 标签:__slots__, 继承

**问**:两个带 __slots__ 的类能同时继承吗?为什么「一个非空 slots + 多个空 slots」可以?

**答**:每个 __slots__ 类有固定的实例布局(没有 __dict__ 的偏移表),多继承两个非空 slots 基类时布局无法合并(TypeError: multiple bases have instance lay-out conflict);空 slots(和 object)不占布局,可以任意混入。规则:slots 继承链最多一个「有字段」的分支,其余必须 __slots__ = ()。另一个隐蔽点:若任一基类没有 slots,子类实例会获得 __dict__,slots 的省内存与防误赋值全部失效;slots 字段名也不能与继承来的字段重复。这些约束是 slots 常在「多继承 + 混入」体系里翻车的原因。

```python
# file: code/01_语言核心与底层/q559_slots_inheritance.py
class A:
    __slots__ = ("a",)

class B:
    __slots__ = ("b",)

class Empty:
    __slots__ = ()

if __name__ == "__main__":
    try:
        class C(A, B):                    # 两个非空 slots 布局冲突
            __slots__ = ("c",)
        print("unexpected success")
    except TypeError as e:
        print("layout conflict:", e)

    class D(A, Empty):                    # 空 slots 可混入
        __slots__ = ("d",)
    d = D()
    d.a, d.d = 1, 2
    print("D fields ok:", d.a, d.d)
    try:
        d.e = 3
    except AttributeError as e:
        print("no dict:", e)
```

**追问**:1) slots 类能和 dataclass 一起用吗?——dataclass(slots=True)(3.10+)会生成带 slots 的新类,但与手写 slots 基类组合时同样受上述布局规则约束,混入一律给空 slots。2) 多继承与 slots 的冲突根源?——实例布局冲突:最多一个基类可有非空 slots,其余基类要么无 slots 要么 slots=(),否则 TypeError(multiple bases have instance lay-out conflict)。3) 底层布局机制?——slots 成员按 MRO 顺序排进固定槽位(描述符 + 偏移),C 结构要求布局唯一;slots 类默认没有 __dict__ 与 __weakref__,要支持需显式声明这两个槽。4) 生产陷阱?——slots 类动态挂属性 AttributeError;weakref 支持缺失让缓存/引用库失效;继承链上漏写父类 slots,子类仍然有 __dict__,省内存优化落空。
