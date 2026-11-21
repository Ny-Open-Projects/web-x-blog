---
title: [Q462] TypedDict 与 total=False
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q462 · TypedDict 与 total=False

> 难度:★★★☆ | 标签:typing, TypedDict

**问**:TypedDict 和普通 dict 加注解有什么区别?运行时它约束了什么?

**答**:TypedDict 声明「这个字典有哪些键、每个键什么类型」,静态检查器据此校验键的存在性与值类型、支持键名自动补全;运行时它就是普通 dict,零开销零强制——多写一个键、漏写一个键,解释器都不拦。`total=False` 声明所有键可选,或用继承把必选/可选分组。适用场景:JSON 边界、函数间传递的结构化字典;需要运行时校验时升级为 pydantic 的 BaseModel 或 dataclass + 校验。

```python
# file: code/01_语言核心与底层/q462_typeddict.py
from typing import TypedDict

class Movie(TypedDict):
    title: str
    year: int

class MoviePartial(TypedDict, total=False):
    """所有字段可选"""
    title: str
    year: int

def print_movie(m: Movie) -> None:
    print(f"{m['title']} ({m['year']})")

if __name__ == "__main__":
    m: Movie = {"title": "Inception", "year": 2010}
    print_movie(m)
    p: MoviePartial = {"title": "Untitled"}     # 缺 year:total=False 允许
    print(p)
    print(type(m).__name__)                     # dict:运行时就是普通字典
    m["extra"] = 1                              # 运行时不拦,mypy 会报错
    print("runtime is permissive:", m)
```

**追问**:1) TypedDict 与 dataclass 怎么选?——数据已有 dict 形态(如 JSON)且想加类型用 TypedDict;要行为、方法、构造校验就用 dataclass;二者可互相转换。2) total=False 与继承怎么组合?——基类声明必选键、total=False 子类声明可选键,静态层按 MRO 合并;3.11+ 的 Required/NotRequired 支持逐键粒度,大型结构更清晰。3) TypedDict 的运行时形态?——它生成一个不可实例化的 dict 子类,类型信息存 __annotations__,get_type_hints 可读;运行时对 TypedDict 做 isinstance 不被支持(3.12 报 TypeError)。4) 生产陷阱?——当运行时校验器用完全不拦;在函数里给入参 TypedDict 塞新键污染下游结构,应返回新 dict;键集合与 API schema 漂移要靠单一来源生成。
