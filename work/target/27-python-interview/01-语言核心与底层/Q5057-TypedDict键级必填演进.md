---
title: [Q5057] TypedDict 的 Required/NotRequired/Unpack 演进
date: 2026-11-20
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5057 · TypedDict 的 Required/NotRequired/Unpack 语义演进

> 难度:★★★★ | 标签:TypedDict, Required, NotRequired, Unpack, 版本演进

**问**：API 客户端 SDK 的参数字典一直用 `Dict[str, Any]`，评审全靠口口相传。TypedDict 从 3.8 到 3.11/3.12 演进了哪些能力？`Required`/`NotRequired` 解决什么矛盾？`Unpack` 又是把什么"升级成了类型"？

**答**：TypedDict 演进三段：a) 3.8 落地，但 `total=True/False` 是**类级开关**——要么全必填要么全可选，表达不了"只有 title 必填"；b) 3.11 的 PEP 655 加入**键级** `Required[k]`/`NotRequired[k]`，可以精确到每个键的必填性，这才让 TypedDict 真正能描述真实 API；c) 3.12 的 PEP 691/696 生态里，`Unpack[MovieTD]` 允许把 TypedDict 展开成 `**kwargs` 的参数类型（配合 `TypeVar` 默认值），SDK 的 `def create(**kwargs: Unpack[MovieParams])` 从此有类型。关键认知：TypedDict 的必填性是**静态层契约**（mypy/pyright 检查），运行时构造 `{"title": "T"}` 不会被任何内置机制校验，`get_type_hints(include_extras=True)` 只能看到 `Required/NotRequired` 包装——运行时校验要交给 Pydantic `TypedDict` 支持或手写校验。所以选型口诀：**跨进程边界用 Pydantic，进程内/SDK 参数形状用 TypedDict**，前者运行时验、后者零运行时成本。

```python
# file: code/01_语言核心与底层/q5057_typeddict.py
import sys
import typing
if sys.version_info < (3, 11):
    raise SystemExit("Required/NotRequired 需要 3.11+, 老版本可用 typing_extensions 等价导入")

from typing import TypedDict, Required, NotRequired, Unpack

# total=False 让所有键默认可选, 再逐键声明必填
class Movie(TypedDict, total=False):
    title: Required[str]          # 必填
    year: int                     # 可选
    rating: NotRequired[float]    # 显式可选(此处与默认一致, 写出来表意)

# total=True(默认)下逐键放行可选
class MovieUpdate(TypedDict):
    title: str
    rating: NotRequired[float]    # 只有 rating 可不传

def create_movie(**kwargs: Unpack[Movie]) -> Movie:
    # Unpack: TypedDict 键名成为 **kwargs 的参数名类型(3.12 语义, mypy/pyright 检查)
    return kwargs

# 运行时不校验: 缺 title 也能构造, 但静态检查会报错
m: Movie = {"title": "T", "year": 2026}
print("合法实例:", m)
print("get_type_hints(include_extras=True):")
for k, t in typing.get_type_hints(Movie, include_extras=True).items():
    print(" ", k, "->", t)   # Required/NotRequired 包装保留在注解层

mv = create_movie(title="T", year=2026)
print("Unpack 传递:", mv)
```

**追问**：1) `TypedDict` 和 `dataclass` 怎么选？——TypedDict 描述"无逻辑的字典形状"（JSON 兼容、kwargs 契约），dataclass 描述"有方法/行为真类"；TypedDict 实例就是普通 dict，没有属性访问、没有运行时校验。2) 递归/可选嵌套 JSON 树用 TypedDict 表达的坑？——自引用要写字符串前向引用且嵌套可选层次爆炸，PEP 747（TypeForm）与 Pydantic `RootModel` 是现状下更工程化的出口；面试答"深层 JSON 用 Pydantic v2 + Annotated"即可。3) `typing_extensions` 的角色？——把新 typing 特性向后移植到 3.8+，库作者按"运行时最低版本 vs 类型检查器支持"两条线选导入源。

## 背诵要点
- 演进链：3.8 TypedDict（total 类级开关）→ 3.11 PEP 655 Required/NotRequired（键级必填）→ 3.12 Unpack（TypedDict 展开 **kwargs）。
- 必填性是静态契约，运行时零校验；跨进程边界用 Pydantic，进程内形状用 TypedDict。
- `get_type_hints(include_extras=True)` 能看到 Required/NotRequired 包装；老版本用 typing_extensions 等价迁移。

## 复盘追问
- 你们的 SDK 参数现在是 Dict[str, Any]，迁 TypedDict 的回归风险在哪？（提示：静态检查新报错风暴——分模块开 strict；运行时行为零变化所以可安全灰度）
- TypedDict 没有运行时校验，误传键名只会在哪一刻暴露？（提示：下游 KeyError/静默忽略，靠单例测试或 Pydantic 边界兜住）
