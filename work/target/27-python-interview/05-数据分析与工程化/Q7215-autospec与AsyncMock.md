---
title: "[Q7215] autospec 对 async 方法生成的是 AsyncMock 吗"
date: 2026-11-23
categories: [Python数据分析工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7215 · autospec 对 async 方法生成的是 AsyncMock 吗

难度：P6 ｜ 标签：pytest、unittest.mock、autospec、AsyncMock

基线：Python 3.12；标准库 `unittest.mock`（`AsyncMock` 3.8+，`autospec` 对协程的支持 3.8+）。

**问**：单测里用 `MagicMock()` 替身一个异步客户端，调用处 `await client.fetch(uid)` 直接报 `TypeError: object MagicMock can't be used in 'await' expression`。换成 `AsyncMock` 能 await 了，但把方法名拼错、参数传错都照样通过，直到线上才炸。`autospec=True` 能同时解决这两个问题吗？它给 async 方法生成的到底是什么？

**答**：
- **结论**：`create_autospec`/`patch(..., autospec=True)` 会按被替身对象的**签名**生成 mock，并且**识别 `async def`，为异步方法生成 `AsyncMock`**（普通方法仍是 `MagicMock`）。所以 `await obj.fetch(uid)` 能正常工作，同时：① 方法名拼错会 `AttributeError`（spec 限制属性集）；② 参数个数/关键字不匹配会 `TypeError`（签名校验）；③ `AsyncMock` 的 `return_value` 是 `await` 之后的普通值，不是协程。
- **取舍**：`autospec` 更安全但更"紧"：动态属性（`__getattr__` 注入、运行时挂载的方法）会被 spec 拒绝，需要 `spec_set=False` 或手动补；对 C 扩展/自带签名的对象，`autospec` 可能拿不到签名而退化。`MagicMock` 宽松、好写，但会让"拼写错误/签名漂移"静默通过，是典型的假绿测试来源。
- **实战**：① 对外部依赖一律 `autospec=True`，内部纯数据对象可用简单 Mock；② 异步方法断言用 `assert_awaited_once_with(...)`，不要用 `assert_called_once_with`（后者对 AsyncMock 仍可用但语义容易混）；③ 需要"调用即抛异常"时用 `side_effect=TimeoutError()`，注意 AsyncMock 会在 await 时抛；④ 定期用 `mypy`/`pyright` 校验调用点，mock 不能替代类型检查。

```python
"""autospec 对 async 方法生成 AsyncMock：签名校验 + 可 await。"""
import asyncio
from unittest.mock import AsyncMock, MagicMock, create_autospec


class UserClient:
    async def fetch(self, uid: int) -> str:
        return f"user-{uid}"

    def close(self) -> None:
        pass


async def main() -> None:
    # 1) 裸 MagicMock：不能 await
    naive = MagicMock()
    try:
        await naive.fetch(1)
    except TypeError as e:
        print("MagicMock await ->", type(e).__name__, str(e)[:40])

    # 2) autospec：异步方法自动变成 AsyncMock
    spec = create_autospec(UserClient, instance=True)
    print("fetch 类型:", type(spec.fetch).__name__)
    spec.fetch.return_value = "cached"
    print("await 结果:", await spec.fetch(1))

    # 3) 签名校验：参数类型/数量不对直接失败
    for bad_call in (lambda: spec.fetch(), lambda: spec.fetch(1, 2)):
        try:
            await bad_call()
        except TypeError as e:
            print("签名校验 ->", str(e)[:50])

    # 4) 属性校验：拼错方法名
    try:
        spec.ftech
    except AttributeError as e:
        print("属性校验 ->", str(e)[:50])

    print("fetch 是否 AsyncMock:", isinstance(spec.fetch, AsyncMock))
    print("close 是否普通 Mock:", type(spec.close).__name__)


if __name__ == "__main__":
    asyncio.run(main())
```

**追问一**：为什么 `AsyncMock` 的 `return_value` 不能设成一个协程？
→ 解析：`AsyncMock` 在 `await` 时会先调用自身、再返回 `return_value`，它已经负责"产生可 await 的结果"。如果你把 `return_value` 设成协程对象，`await` 得到的是协程本身，调用方再 `await` 就会报 "coroutine is not awaitable" 或得到错误类型。正确做法是直接设普通值，或用 `side_effect` 提供异步函数。

**追问二**：`autospec` 和 `spec_set` 有什么区别，什么时候会失效？
→ 解析：`spec` 只校验"读属性"的集合与签名，仍允许**写**不存在的属性；`spec_set` 连写也禁止，更严格。`autospec` 是"生成带 spec 的 mock"的工厂。失效场景：对象用 `__getattr__` 动态生成属性、C 扩展对象无 `__signature__`、`functools.partial`/装饰器丢失签名——这时 autospec 会拒绝或退化，需要手动 `spec=` 或改造成可测的显式接口。
