---
title: [Q5138] typing 注解的运行时成本与缓存
date: 2026-11-21
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5138 · typing 注解的运行时成本与缓存

难度：P6 | 标签：typing、get_type_hints、PEP 563/649、成本工程

**问**：注解不是"只是提示"吗？为什么有些服务加上大量泛型注解后启动时间和每请求耗时都涨了？请拆解 typing 在运行时的真实成本点（注解求值、get_type_hints、isinstance 与泛型的边界），并给出控制成本的实践。

**答**：

**结论**：成本点有三层。(1) **定义成本**：模块导入时 `List[Dict[str, int]]` 这类下标表达式会真实执行、创建 `_GenericAlias` 对象，成千上万个复杂注解直接拖慢启动；PEP 563（`from __future__ import annotations`，字符串化）把求值推迟到访问时，PEP 649（Python 3.14 默认）改为惰性注解求值，从语言层面缓解。(2) **解析成本**：`typing.get_type_hints` 每次调用都要对字符串注解做 eval + 递归展开泛型参数，框架（Pydantic、FastAPI）靠内部缓存扛住，自己裸调则每请求都是重放。(3) **检查成本**：`isinstance(x, List[int])` 会抛 TypeError——泛型参数不参与运行时 isinstance，只有 `isinstance(x, list)` 或经过 `__class_getitem__` 特殊处理的类型（如 `collections.abc.Callable[...]` 不行，`typing.Union` 经由 `__instancecheck__` 可以）可用，误用检查反而引入 try/except 开销。

**取舍**：运行时用注解的框架必须缓存解析结果（Pydantic v2 在模型类创建时一次性编译校验器）；纯类型检查用途的注解走字符串化最便宜。别用 typing 别名做高频路径的运行时判断，成本敏感处用 `typing.get_origin/get_args` 一次性预判并缓存。

**实战**：基线：示例基于 Python 3.12；3.14 起 PEP 649/749 落地后 `__annotations__` 变为惰性描述符，`get_type_hints` 的行为差异要回归（3.13 及以下加 `from __future__ import annotations` 需自备求值环境）。

```python
import timeit, sys
print("python", sys.version.split()[0])

# 1) 定义成本：泛型下标在导入期真实执行
t = timeit.timeit("from typing import List, Dict; List[Dict[str, List[int]]]",
                  number=100_000)
print(f"创建 10 万个复杂注解对象: {t*1000:.0f} ms")

# 2) 字符串化（PEP 563）后的解析成本：get_type_hints 每次都要 eval
from typing import get_type_hints

def parse_cost():
    ns = {"__name__": "order_mod"}
    src = ("from __future__ import annotations\n"
           "from typing import List, Dict\n"
           "class Order:\n"
           "    items: 'List[Dict[str, float]]'\n")
    exec(src, ns)
    cls = ns["Order"]
    first = timeit.timeit(
        lambda: get_type_hints(cls, globalns=ns), number=1)
    # 框架级做法：解析一次缓存
    cached = get_type_hints(cls, globalns=ns)
    return first, cached

first, _ = parse_cost()
print(f"get_type_hints 首次解析(含 eval): {first*1000:.2f} ms —— 务必缓存")

# 3) isinstance 与泛型的边界
import typing
try:
    isinstance([1], typing.List[int])
except TypeError as e:
    print("泛型 isinstance ->", e)
print("运行时判别用 get_origin/get_args:",
      typing.get_origin(typing.List[int]), typing.get_args(typing.List[int]))
```

**追问 1**：`from __future__ import annotations` 有哪些坑？
答：注解变字符串后，运行时框架若直接读 `__annotations__` 拿到的是 str 而不是类型对象，必须经 `get_type_hints`（需要名字可见）；局部类/闭包内定义的类求值时可能 NameError。

**追问 2**：为什么 dataclass 处理注解比手写框架快？
答：dataclass 在类创建时同步解析注解并生成 `__init__`，属"一次性编译"；而某些框架在第一次请求时才解析，把成本摊到热路径——启动慢和请求慢，是同一成本的不同摊销位置。

**追问 3**：`typing.get_origin(List[int])` 返回什么？3.8-3.11 与 3.12 有差异吗？
答：返回 `list`（未参数化的 `typing.List` 在 3.9+ 已别名到内置 list）；3.8 返回 `typing.List` 需要额外判断，跨版本写兼容代码时统一用 `get_origin` 并对 `None`（裸类）分支。

## 背诵要点

- 注解下标在导入期真实创建对象（定义成本）；PEP 563 字符串化、3.14 PEP 649 惰性化是演进方向。
- get_type_hints 每次调用都 eval+展开，必须缓存——框架慢多半是解析成本摊销位置不对。
- 泛型参数不参与 isinstance；运行时判别用 get_origin/get_args 预判并缓存。

## 复盘追问

- FastAPI 依赖注入为什么重注解接口比轻注解接口启动慢数秒？(提示：路由建立期 get_type_hints 风暴)
- 如何给"注解解析耗时"建观测？(提示：importtime + 类创建期打点)
