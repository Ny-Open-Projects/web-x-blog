---
title: [Q2616] get_origin 与 get_args:泛型的运行时拆解
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2616 · get_origin 与 get_args:泛型的运行时拆解

> 难度:★★★☆☆ | 标签:typing, 泛型, 运行时内省

**问**:`List[int]` 在运行时是个什么对象?怎么把它的下标参数拆出来?

**答**:泛型别名是 `typing._GenericAlias` 对象,标准库给的两个拆解入口是 `typing.get_origin` 和 `typing.get_args`:`get_origin(List[int])` 返回未参数化的 `list`,`get_args` 返回 `(int,)`;对联合类型,origin 是 `typing.Union`、args 是成员元组。3.9 起内置类型直接支持下标(PEP 585),`list[int]` 与 `typing.List[int]` 都能这样拆。重要边界:`isinstance(x, List[int])` 会直接抛 TypeError,因为运行时判定参数化泛型没有意义——正确做法是先用 `get_origin` 拿回裸类型再 isinstance。这套工具是写序列化框架、依赖注入容器时做「注解驱动」开发的标配。

```python
# file: code/01_语言核心与底层/q2616_get_origin_args.py
"""get_origin 与 get_args:把泛型别名拆回裸类型与参数。"""
import typing
from typing import Dict, List, Union, get_args, get_origin


def check_str_list(obj):
    """运行时校验 obj 是 list 且元素都是 str,不使用参数化泛型 isinstance。"""
    origin = get_origin(List[str])            # list
    if not isinstance(obj, origin):
        return False
    return all(isinstance(item, str) for item in obj)


if __name__ == "__main__":
    print("origin List[int]:", get_origin(List[int]))          # list
    print("args   List[int]:", get_args(List[int]))            # (int,)
    print("origin Dict[str, int]:", get_origin(Dict[str, int]))
    print("args   Dict[str, int]:", get_args(Dict[str, int]))
    print("origin Union[str, int]:", get_origin(Union[str, int]))
    print("args   Union[str, int]:", get_args(Union[str, int]))

    print("内置泛型 list[int]:", list[int], get_args(list[int]))

    try:
        isinstance([], List[int])
    except TypeError as exc:
        print("参数化泛型 isinstance 被拒:", exc)

    print("check_str_list(['a', 1]):", check_str_list(["a", 1]))
    print("check_str_list(['a', 'b']):", check_str_list(["a", "b"]))
```

**追问**:1) 为什么参数化泛型不能用于 isinstance?——运行时容器并不记录元素类型,`List[int]` 与 `List[str]` 的运行时对象没有区别,参数只是给静态检查器看的元数据。2) 拆解的实际用途?——框架读 `Optional[X]` 的 __origin__/__args__ 做运行时反射(pydantic/DRF);get_type_hints 配合解析字符串注解(Q499);GenericAlias 的本质是元数据壳。3) isinstance 的合法替代?——isinstance(x, list) 查容器 + 逐元素检查;类型变量化校验交给静态层或 pydantic;3.10+ 部分 GenericAlias 形式(如 list[int])可用 isinstance,但不含元素语义。4) 生产陷阱?——写 isinstance(x, List[int]) 直接 TypeError;期望运行时校验元素类型;把泛型别名传给需要真实类型的 API。
