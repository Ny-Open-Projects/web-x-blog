---
title: [Q1268] 递归类型别名:JSON 树怎么表达
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1268 · 递归类型别名:JSON 树怎么表达

> 难度:★★★★☆ | 标签:typing, 递归类型

**问**:JSON 的类型是「值里套值」,type hint 怎么写递归结构?3.12 的 `type` 语句好在哪?

**答**:递归别名靠前向引用:模块级 `JSON = Union[None, bool, int, float, str, List["JSON"], Dict[str, "JSON"]]`,字符串形式让别名先定义后引用,静态检查器与 `typing.get_type_hints` 都能解开。运行时这个别名只是个普通 Union 对象,可以拿来做 isinstance 风格的递归校验。痛点是老语法笨重且不能带类型参数;3.12 的 PEP 695 `type JSON = None | bool | int | float | str | list[JSON] | dict[str, JSON]` 把递归别名变成一等语法——作用域干净、惰性求值、支持泛型参数(type Tree[T] = ...),建议新项目按版本采用。工程上真正的坑在验证器:递归结构必须递归校验且注意深度(见 Q1299 的爆栈)。

```python
# file: code/01_语言核心与底层/q1268_recursive_alias.py
import json
from typing import Dict, List, Union

JSON = Union[None, bool, int, float, str,
             List["JSON"], Dict[str, "JSON"]]     # 字符串前向引用,3.9 可用


def validate(obj) -> bool:
    if obj is None or isinstance(obj, (bool, int, float, str)):
        return True
    if isinstance(obj, list):
        return all(validate(x) for x in obj)
    if isinstance(obj, dict):
        return all(isinstance(k, str) and validate(v) for k, v in obj.items())
    return False


if __name__ == "__main__":
    doc = json.loads('{"a": [1, 2.5, null, true], "b": {"c": "text"}}')
    print("valid doc  :", validate(doc))
    print("invalid doc:", validate({1: "x"}))
    print("alias type :", type(JSON).__name__, "| 递归成员可解开")
    if __import__("sys").version_info >= (3, 12):
        print("3.12+: type JSON = ... 一等递归别名语法")
```

**追问**:1) typing.get_type_hints 能解开这个别名吗?——能,它会递归求值 ForwardRef;但对「类型变量指向自身」的病态定义会抛 RecursionError,递归别名必须有基例。2) 为什么要显式别名语法?——裸赋值有「变量还是别名」歧义;3.10 用 `X: TypeAlias = ...`,3.12 的 `type X = ...` 内建惰性求值,递归定义不再需要字符串。3) 惰性机制?——3.12 TypeAliasType 按需展开,3.10- 靠字符串前向引用 + get_type_hints 解析;递归结构的基例(标量/空)必须有,否则解析不终止。4) 生产陷阱?——运行时解析深层递归别名性能差甚至爆栈;3.10 无 type 语法时字符串引用易拼错;别名与 JSON schema 两处维护漂移。
