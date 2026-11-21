---
title: [Q463] @overload:类型层面的重载
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q463 · @overload:类型层面的重载

> 难度:★★★★ | 标签:typing, overload

**问**:Python 运行时不支持重载,@overload 到底「重载」了什么?

**答**:@overload 声明的是「同一个名字在不同参数类型下的返回类型关系」,纯静态概念:装饰器把这些桩注册起来供 mypy 匹配调用点,真正的实现是随后不带 @overload 的同名 def,运行时只有它存在。典型用途:同一函数按参数类型返回不同类型(str 进 list 出、int 进 str 出),或可选参数组合的精确签名。运行时不再做类型分派,分支逻辑靠 isinstance 写在实现里;@singledispatch 才是运行时真分派,两者互补。

```python
# file: code/01_语言核心与底层/q463_overload.py
from typing import overload

@overload
def parse(value: str) -> list:
    """字符串:按逗号拆分为列表"""

@overload
def parse(value: int) -> str:
    """整数:格式化为编号"""

def parse(value):
    """运行时唯一存在的实现"""
    if isinstance(value, str):
        return value.split(",")
    if isinstance(value, int):
        return f"code-{value}"
    raise TypeError(f"unsupported: {type(value).__name__}")

if __name__ == "__main__":
    print(parse("a,b,c"))
    print(parse(7))
    try:
        parse(1.5)
    except TypeError as e:
        print("runtime rejects:", e)
    print("overloads are invisible at runtime:", parse.__name__)
```

**追问**:1) @overload 的桩如果被意外调用会怎样?——typing.overload 返回的占位函数会抛 NotImplementedError,说明调用路径错到了声明桩上,通常是实现没写或被覆盖顺序写反。2) overload 与 singledispatch 的分工?——overload 是静态层「签名-返回关系表」,运行时不存在;functools.singledispatch 按首参类型运行时真分派。要精确返回类型用 overload,要插件式分派用 singledispatch。3) 桩的去向?——typing.overload 把桩存进 __overloads__ 供检查器读取,返回抛 NotImplementedError 的占位;随后的同名实现 def 覆盖模块命名空间绑定,运行时只有实现存在。4) 生产陷阱?——实现签名比所有桩都宽,调用点类型不匹配时报 "no overload variant matches";桩写了函数体会误导读者以为它可调用——桩只有签名没有体。
