---
title: [Q5008] PEP 696 TypeVar 默认值与泛型协议实战
date: 2026-11-18
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5008 · PEP 696 TypeVar 默认值与泛型协议实战

> 难度:★★★ | 标签:PEP 696, TypeVar, 泛型

**问**：PEP 696（3.13）给 TypeVar/ParamSpec 加了默认值，解决什么真实痛点？`T = TypeVar("T", default=str)` 在运行时和检查器两侧分别怎么生效？设计泛型容器/客户端基类时默认值怎么用才不出事故？

**答**：结论：痛点是**裸泛型引用**——旧写法里 `class Client[SessionT]` 被 `Client`（不带参数）引用时检查器报错或推成 `Unknown`，逼着使用者到处写 `Client[NullSession]`。PEP 696 允许 `SessionT = TypeVar("SessionT", default=NullSession)`：裸引用 `Client` 时自动取默认，显式 `Client[RedisSession]` 时用实参。运行时表现：3.13 的 `typing.TypeVar` 接受 `default=` 关键字（`TypeVar.__default__`），`Generic`/`Protocol` 解析裸参数时读它；`get_type_hints` 与 `__type_params__` 链路都能拿到。设计纪律三条：1) 默认值选「最无害」的形态（NullSession / None / 空回调），让裸引用安全；2) **默认值本身也要是类型**——写成 `default=None`（值 None 而非类型 NoneType）会被检查器拒，要写 `NoneType` 或 `X | None`；3) Variance 不受默认影响，但默认类型必须满足 variance 约束（协变 TypeVar 的默认必须也在协变位置合法）。实战陷阱：默认值是「检查期填充」，运行时 `Client.__class_getitem__` 裸访问（3.13 起 `Client[...]` 不写参数时泛型别名/类才用默认）——依赖 `__orig_class__` 的运行时代码在裸引用下拿到的是带默认的参数化类型，别再假设它一定被显式指定。

```python
# 基线:Python 3.13+(PEP 696)。3.12 及以下缺库降级:
# 用两个显式类(Client 与 NullClient)或 ClassVar 哨兵模拟默认形态。
import sys
from typing import Generic, TypeVar

class NullSession:
    """默认形态:什么都不做,保证裸引用 Client 安全。"""

class RedisSession:
    def __init__(self) -> None:
        self.name = "redis"

if sys.version_info >= (3, 13):
    SessionT = TypeVar("SessionT", default=NullSession)  # PEP 696 默认值

    class Client(Generic[SessionT]):
        def __init__(self, session: SessionT | None = None) -> None:
            self.session = session

    c0: Client = Client()                 # 裸引用 → 默认 NullSession
    c1: Client[RedisSession] = Client(RedisSession())
    print(SessionT.__default__ is NullSession)   # True
else:
    print("3.12-: 无 default=;退化为 Client 与 NullClient 两个类")
```

**追问**：
1) ParamSpec 的默认值怎么写？——`P = ParamSpec("P", default=...)` 用省略号字面量表示「默认捕获任意签名」，装饰器工厂 `decorator` 裸引用时保持原函数签名，这是「保留签名的装饰器默认形态」的标准写法。
2) TypeVarTuple 能有默认值吗？——可以，`Ts = TypeVarTuple("Ts", default=Unpack[tuple[int, ...]])` 之类，但组合（默认与实参混排）的解析顺序由检查器裁，运行时不参与——默认值是纯静态语义，运行时只在 `__default__` 上可见。
3) 默认值会不会让「漏写参数」的错误静默？——会，这是主要取舍：默认值消除了裸引用报错，也让「本该显式指定」的地方静默通过。缓解：默认形态选运行时即失败或可观测的哨兵（NullSession 在被使用时打日志/抛错），让静默变成显式故障。
