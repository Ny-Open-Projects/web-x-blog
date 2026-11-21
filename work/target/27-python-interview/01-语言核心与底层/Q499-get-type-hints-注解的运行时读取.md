---
title: [Q499] get_type_hints:注解的运行时读取
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q499 · get_type_hints:注解的运行时读取

> 难度:★★★☆ | 标签:typing, 注解

**问**:func.__annotations__ 和 get_type_hints(func) 有什么区别?字符串注解为什么要延迟求值?

**答**:__annotations__ 是原始存储:字符串形式的注解(前向引用 "MyClass"、from __future__ import annotations 下的全部字符串)原样躺着;get_type_hints 负责在函数的 globals 命名空间里求值,还原成真实类型对象,并处理 Optional 等语法糖。延迟求值的动机:前向引用不需要引号 hack、加速模块导入、规避循环导入。框架在运行时消费注解(pydantic/FastAPI)一律走 get_type_hints;注意 3.10+ 某些联合类型形式(如 int | None 的 __annotations__ 值)是 types.UnionType 而不是 typing.Union,判型要两者都兼容。

```python
# file: code/01_语言核心与底层/q499_get_type_hints.py
from typing import Dict, List, get_type_hints

def parse(data: "bytes") -> "Dict[str, int]":
    """字符串注解:运行时延迟求值"""
    return {}

def summarize(rows: List[Dict[str, float]], title: str = "report") -> str:
    return f"{title}: {len(rows)} rows"

if __name__ == "__main__":
    print("raw annotations:", parse.__annotations__)
    print("resolved:", get_type_hints(parse))
    hints = get_type_hints(summarize)
    print("rows origin:", hints["rows"].__origin__)
    print("title default preserved:", summarize.__defaults__)
```

**追问**:1) 为什么 dataclasses 和 pydantic 对注解求值时机敏感?——它们在类创建时读注解生成字段,前向引用的字段若 get_type_hints 时仍解析不到(循环导入)就报错,模块组织要保证类型定义先行。2) 为什么不能直接读 __annotations__?——注解可能是字符串(前向引用或 from __future__ import annotations),get_type_hints 负责 eval 解析(globalns/localns);裸读拿到字符串无法用于校验。3) 解析的底层机制?——__annotations__ 在类/模块创建时记录原始表达式;get_type_hints 递归展开 Optional/Annotated,名字缺失抛 NameError——所以前向引用必须在调用时可见。4) 生产陷阱?——循环导入让 get_type_hints 运行时 NameError 而不是 import 期;函数内取 hint 忘传 localns;3.10 不加 future 时混用运行时对象与字符串注解,工具行为分裂。
